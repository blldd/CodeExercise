import java.io.File;
import java.io.IOException;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;

public class JsonParser {
	static String str = "{\"fileName\" : \"a\", \"isFolder\" : true, \"files\" : ["
			+ "{\"fileName\" : \"b\", \"isFolder\" : true, \"files\" : ["
			+ "{\"fileName\" : \"c.txt\", \"isFolder\" : false},"
			+ "{\"fileName\" : \"d.txt\", \"isFolder\" : false},"
			+ "{\"fileName\" : \"e\", \"isFolder\" : true}"
			+ "]}"
			+ "{\"fileName\" : \"f.txt\", \"isFolder\" : false},"
			+ "{\"fileName\" : \"g.txt\", \"isFolder\" : false}"
			+ "]}";
	static JSONObject object = JSONObject.parseObject(str);
	public static void main(String[] args) throws IOException {
		String path = "E:\\eclipsemarsworkspace\\";
		if((boolean) object.get("isFolder")){
			createFolder(path, (String) object.get("fileName"), object);
		} else {
			createFile(path, (String) object.get("fileName"));
		}
	}
	private static void createFile(String path, String str) throws IOException {
		File file = new File(path, str);
		file.createNewFile();
	}
	private static void createFolder(String path, String str, JSONObject obj) throws IOException {
		File file = new File(path, str);
		file.mkdir();
		path = path + str + "\\";
		if(((JSONObject) obj).get("files") != null){
			JSONArray array = (JSONArray) obj.get("files");
			for(int i = 0; i < array.size(); i++){
				JSONObject subObject = (JSONObject) array.get(i);
				if((boolean) subObject.get("isFolder")){
					createFolder(path, (String) subObject.get("fileName"), subObject);
				} else {
					createFile(path, (String) subObject.get("fileName"));
				}
			}
		}
	}
}