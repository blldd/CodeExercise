import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()

        self.d_model = d_model
        self.num_heads = num_heads

        self.query_fc = nn.Linear(d_model, d_model)
        self.key_fc = nn.Linear(d_model, d_model)
        self.value_fc = nn.Linear(d_model, d_model)

        self.softmax = nn.Softmax(dim=-1)
        self.output_fc = nn.Linear(d_model, d_model)

    def forward(self, query, key, value, mask=None):
        # query, key, value shape: (batch_size, seq_len, d_model)

        batch_size = query.shape[0]

        # Linear transformations
        query = self.query_fc(query)  # (batch_size, seq_len, d_model)
        key = self.key_fc(key)  # (batch_size, seq_len, d_model)
        value = self.value_fc(value)  # (batch_size, seq_len, d_model)

        # Reshape to perform multi-head attention
        query = query.view(batch_size, -1, self.num_heads, self.d_model // self.num_heads)
        key = key.view(batch_size, -1, self.num_heads, self.d_model // self.num_heads)
        value = value.view(batch_size, -1, self.num_heads, self.d_model // self.num_heads)

        # Transpose to perform batch-wise dot product
        query = query.transpose(1, 2)  # (batch_size, num_heads, seq_len, d_model // num_heads)
        key = key.transpose(1, 2)  # (batch_size, num_heads, seq_len, d_model // num_heads)
        value = value.transpose(1, 2)  # (batch_size, num_heads, seq_len, d_model // num_heads)

        # Compute attention scores
        scores = torch.matmul(query, key.transpose(-2, -1))  # (batch_size, num_heads, seq_len, seq_len)
        scores = scores / (self.d_model // self.num_heads) ** 0.5

        # Apply mask (if provided)
        if mask is not None:
            mask = mask.unsqueeze(1).unsqueeze(1)  # (batch_size, 1, 1, seq_len)
            scores = scores.masked_fill(mask == 0, float('-inf'))

        # Compute attention weights
        weights = self.softmax(scores)  # (batch_size, num_heads, seq_len, seq_len)

        # Apply attention weights
        attention_output = torch.matmul(weights, value)  # (batch_size, num_heads, seq_len, d_model // num_heads)

        # Concatenate and reshape attention output
        attention_output = attention_output.transpose(1, 2)  # (batch_size, seq_len, num_heads, d_model // num_heads)
        attention_output = attention_output.reshape(batch_size, -1, self.d_model)

        # Apply linear transformation to attention output
        output = self.output_fc(attention_output)  # (batch_size, seq_len, d_model)

        return output
