package com.sample.autocode.utils;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.ObjectOutputStream;
import java.util.LinkedList;

public class FileUtils {

	public static String readFile(String Path) {
		BufferedReader reader = null;
		String laststr = "";
		try {
			System.out.println("开始读文件......");
			FileInputStream fileInputStream = new FileInputStream(Path);
			InputStreamReader inputStreamReader = new InputStreamReader(fileInputStream, "UTF-8");
			reader = new BufferedReader(inputStreamReader);
			String tempString = null;
			while ((tempString = reader.readLine()) != null) {
				laststr += tempString;
			}
			reader.close();
			System.out.println("文件读取完毕......");
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (reader != null) {
				try {
					reader.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		return laststr;
	}

	public static <E> void writeObj2File(String path, LinkedList<E> msg) {
		File file = new File(path);

		if (!file.exists()) {
			try {
				file.createNewFile();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}


		try {
			// The value "false" for FileOutputStream means that overwrite this
			// file,
			// if it is "true",append the new data to this file.
			ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(file, false));
			oos.writeObject(msg);
			oos.flush();
			oos.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

}
