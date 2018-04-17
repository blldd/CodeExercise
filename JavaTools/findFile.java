import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;
/***
 * 
 * @author Don
 * 
 *give a num n; m is fileNum; find the file which meets n % m == N % m
 */
public class FindFile {
	static String path = "E:\\eclipsemarsworkspace\\test\\";
	static int fileNum;
	static int re;
	static ArrayList array = new ArrayList();

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int inputNum = sc.nextInt();
		File file = new File(".");
		String[] fileList = file.list();
		fileNum = fileList.length;
		re = inputNum % fileNum;
		String findFileName = fileList[re - 1];
		readFile(findFileName);
	}

	private static void readFile(String string) throws IOException {
		array.add(string);
		if(array.size() == fileNum){
			System.out.println("not found");
			
		}
		FileInputStream fis = new FileInputStream(path + string);
		InputStreamReader reader = new InputStreamReader(fis);
		BufferedReader br = new BufferedReader(reader);
		String line = br.readLine();
		String[] semiSplit = line.split(";");
		int N = Integer.parseInt(semiSplit[1].trim());
		int result = N % fileNum;
		String[] slashSplit = semiSplit[0].split(" ");
		if (re == result) {
			System.out.println(path + string);
		} else {
			for (String name : slashSplit) {
				if (array.contains(name)) {
					continue;
				} else {
					readFile(name);
				}
			}
		}
	}
}