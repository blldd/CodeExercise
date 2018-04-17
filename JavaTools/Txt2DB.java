package ecnu.nlp.controller;

import java.io.File;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import org.apache.commons.io.FileUtils;
import org.apache.commons.io.LineIterator;

/**
 * Created by Don on 2017/8/30.
 */

public class Txt2DB {

    int idx;
    Connection conn = null;
    PreparedStatement pstmt = null;

    // 使用commons-io.jar包的FileUtils的类进行读取
    public void readTxtFileByFileUtils(String fileName) {
        File file = new File(fileName);

        dbConnection();

        try {
            LineIterator lineIterator = FileUtils.lineIterator(file, "GB2312");
            while (lineIterator.hasNext()) {
                String line1 = lineIterator.nextLine();
                String line2 = lineIterator.nextLine();
//                String[] custArray = line.split("\\|");

                String[] custArray = new String[2];
                custArray[0] = line1;
                custArray[1] = line2;
                insertCustInfo(custArray);

                Thread.sleep(10);

            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            dbDisConnection();
        }
    }

    // 插入到数据库中
    public void insertCustInfo(String[] strArray) {
        try {
            StringBuffer sqlBf = new StringBuffer();
            sqlBf.setLength(0);

            sqlBf.append("INSERT INTO SYNONYM(KEYWORD, SYNONYM)                \n");
            sqlBf.append("          VALUES(?                                                    \n");
            sqlBf.append("               , ?)                                                   \n");

            pstmt = conn.prepareStatement(sqlBf.toString());
            idx = 1;
            pstmt.clearParameters();
//            pstmt.setInt(idx++, Integer.parseInt(strArray[0]));
            pstmt.setString(idx++, strArray[0]);
            pstmt.setString(idx++, strArray[1]);

            pstmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            if (pstmt != null) {
                try {
                    pstmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    // 连接数据库
    public Connection dbConnection() {
        try {
            Class.forName("com.mysql.jdbc.Driver");

            String url = "jdbc:mysql://localhost:3306/customs";
            String user = "root";
            String password = "ecnunlp";

            conn = DriverManager.getConnection(url, user, password);
            System.out.println("Connection 开启！");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return conn;
    }

    // 关闭数据库
    public void dbDisConnection() {
        if (conn != null) {
            try {
                conn.close();
                System.out.println("Connection 关闭！");
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        Txt2DB t = new Txt2DB();
        t.readTxtFileByFileUtils("G:\\Projects\\Haiguan\\syn_result.txt");
//        rcf.readTxtFileByFileUtils("G:\\Projects\\Haiguan\\test.txt");
    }
}