package com.sample.autocode.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class BaseDao {

	public static final String DRIVER_NAME = "com.mysql.jdbc.Driver";
	public static final String DB_NAME = "phone_no_lib";
	public static final String URL = "jdbc:mysql://127.0.0.1:3306/" + DB_NAME + "?characterEncoding=UTF8";
	public static final String DB_USER = "root";
	public static final String DB_PWD = "root";

	private static Connection conn = null;
	private static PreparedStatement ps = null;

	private static ResultSet rs = null;

	public static void getConnection() {

		try {
			Class.forName(DRIVER_NAME);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		try {
			conn = DriverManager.getConnection(URL, DB_USER, DB_PWD);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public static void closeAll() {
		if (rs != null)
			try {
				rs.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		if (ps != null)
			try {
				ps.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		if (conn != null)
			try {
				conn.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	}

	public static ResultSet executeQuery(String sql, String[] parameters) {
		try {
			ps = conn.prepareStatement(sql);
			if (parameters != null && !parameters.equals("")) {
				for (int i = 0; i < parameters.length; i++) {
					ps.setString(i + 1, parameters[i]);
				}
			}
			rs = ps.executeQuery();
		} catch (Exception e) {
			e.printStackTrace();
			throw new RuntimeException(e.getMessage());
		}

		return rs;
	}

	public static void update(String sql, String[] parmeters) {
		try {
			ps = conn.prepareStatement(sql);
			if (parmeters != null) {
				for (int i = 0; i < parmeters.length; i++) {
					ps.setString(i + 1, parmeters[i]);
				}
			}
			ps.executeUpdate();
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
