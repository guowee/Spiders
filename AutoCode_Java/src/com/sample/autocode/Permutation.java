package com.sample.autocode;

import java.util.ArrayList;
import java.util.List;

import com.sample.autocode.dao.BaseDao;
import com.sample.autocode.entity.Permutate;

public class Permutation {

	private static List<Permutate> list = new ArrayList<Permutate>();

	public static void main(String[] args) {

		try {
			System.out.println("连接数据库......");
			BaseDao.getConnection();

			for (int i = 0; i < 10; i++) {
				for (int j = 0; j < 10; j++) {
					for (int m = 0; m < 10; m++) {
						for (int n = 0; n < 10; n++) {
							list.add(new Permutate("" + i + j + m + n + ""));
						}

					}

				}

			}

			String sql = "insert into web$tail_number(tail) values(?)";
			System.out.println("开始向数据库中插入数据......");
			for (Permutate obj : list) {
				String[] parmeters = { obj.getTail() };
				BaseDao.update(sql, parmeters);
			}
			System.out.println("插入数据完毕！");
		} catch (Exception e) {
			e.printStackTrace();

		} finally {

			BaseDao.closeAll();
		}

	}

}
