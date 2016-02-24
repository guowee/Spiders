package com.sample.autocode;

import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.sample.autocode.dao.BaseDao;
import com.sample.autocode.entity.Autocode;
import com.sample.autocode.utils.FileUtils;

import net.sf.json.JSONArray;

public class AutoCodeParse {
	private static List<Autocode> list = new ArrayList<Autocode>();
	private static Gson gson = new Gson();

	public static void main(String[] args) {

		String filename = "assets/items.json";
		String json = FileUtils.readFile(filename);
		JSONArray jsonArray = JSONArray.fromObject(json);
		for (Object obj : jsonArray) {
			Autocode code = gson.fromJson(obj.toString(), Autocode.class);
			list.add(code);
		}
		try {
			System.out.println("连接数据库......");
			BaseDao.getConnection();

			String sql = "insert into web$auto_phone_code(province,city,isp,code) values(?,?,?,?)";
            System.out.println("开始向数据库中插入数据......");
			for (Autocode obj : list) {
				String[] parmeters = { obj.getProvince(), obj.getCity(), obj.getIsp(), obj.getCode() };
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
