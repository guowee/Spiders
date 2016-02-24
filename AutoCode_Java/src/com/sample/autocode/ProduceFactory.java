package com.sample.autocode;

import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import com.sample.autocode.dao.BaseDao;
import com.sample.autocode.entity.Autocode;
import com.sample.autocode.entity.Permutate;
import com.sample.autocode.utils.FileUtils;

public class ProduceFactory {

	public static List<Autocode> codeList = new ArrayList<Autocode>();
	public static List<Permutate> tailList = new ArrayList<Permutate>();
	public static List<Autocode> totalList = new ArrayList<Autocode>();
	public static LinkedList<Autocode> list=new LinkedList<Autocode>();
	public static void main(String[] args) {
		try {
			System.out.println("连接数据库......");
			BaseDao.getConnection();
            System.out.println("开始查询移动code码");
			String sql1 = "select * from web$auto_phone_code where isp=?";
			String[] parameters = { "移动" };
			ResultSet rs = BaseDao.executeQuery(sql1, parameters);
			while (rs.next()) {
				Autocode code = new Autocode();
				code.setId(rs.getInt("id"));
				code.setProvince(rs.getString("province"));
				code.setCity(rs.getString("city"));
				code.setCode(rs.getString("code"));
				code.setIsp(rs.getString("isp"));
				codeList.add(code);
			}
			System.out.println("开始查询尾号");
			String sql2 = "select * from web$tail_number ";
			String[] parameters2 = null;
			ResultSet rs2 = BaseDao.executeQuery(sql2, parameters2);
			while (rs2.next()) {
				Permutate permutate = new Permutate();

				permutate.setId(rs2.getInt("id"));
				permutate.setTail(rs2.getString("tail"));
				tailList.add(permutate);
			}
			String sql = "insert into web$total_phone_number(province,city,isp,phoneno) values(?,?,?,?)";
			System.out.println("开始向数据库中插入数据......");
			for (Autocode code : codeList) {
				for (Permutate permutate : tailList) {
					String number = code.getCode() + permutate.getTail();
					Autocode totalCode = new Autocode(code.getProvince(), code.getCity(), number, code.getIsp());
					list.add(totalCode);
					
					//String[] parmeters = { totalCode.getProvince(), totalCode.getCity(), totalCode.getIsp(), totalCode.getCode() };
					//BaseDao.update(sql, parmeters);

				}
				System.out.println("------------");
				FileUtils.writeObj2File("F://data/data.csv",list);
			}

			System.out.println("插入数据完毕！");
		} catch (Exception e) {
			e.printStackTrace();

		} finally {

			BaseDao.closeAll();
		}

	}

}
