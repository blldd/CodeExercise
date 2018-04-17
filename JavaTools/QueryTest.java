
import org.apache.commons.io.FileUtils;
import org.apache.commons.io.LineIterator;

import java.io.File;
import java.io.IOException;
import java.sql.*;

/**
 * Created by Don on 2017/8/30.
 */
public class QueryTest {

    int idx;
    Connection conn = null;
    PreparedStatement pstmt = null;

    // 使用commons-io.jar包的FileUtils的类进行读取
    public void searchByKW(String k) {

        try {
            String sql = "select * from synonym s WHERE s.keyWord = ?";
            pstmt = conn.prepareStatement(sql); //创建Statement对象
            pstmt.setString(1, k);

            //要执行的SQL
            ResultSet rs = pstmt.executeQuery();//创建数据对象
            while (rs.next()){
                System.out.print(rs.getString(1) + "\t");
                System.out.print(rs.getString(2) + "\t");
                System.out.println();
            }
            rs.close();
            pstmt.close();

        } catch (SQLException e) {
            e.printStackTrace();
        }
//        finally {
//            dbDisConnection();
//        }
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
        QueryTest q = new QueryTest();

        q.dbConnection();

        long startMili=System.currentTimeMillis();// 当前时间对应的毫秒数
        System.out.println("开始 "+startMili);

        for (int i = 0; i < 1000; i++){
            q.searchByKW("大家");
        }

        long endMili=System.currentTimeMillis();
        System.out.println("结束 "+endMili);
        System.out.println("总耗时为："+(endMili-startMili)+"毫秒");

        q.dbDisConnection();
    }
}