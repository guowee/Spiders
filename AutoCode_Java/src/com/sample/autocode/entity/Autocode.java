package com.sample.autocode.entity;

import java.io.Serializable;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Autocode implements Serializable {
	@Expose
	@SerializedName("id")
	private Integer id;

	@Expose
	@SerializedName("province")
	private String province;
	@Expose
	@SerializedName("city")
	private String city;
	@Expose
	@SerializedName("code")
	private String code;
	@Expose
	@SerializedName("isp")
	private String isp;

	public Autocode() {

	}

	public Autocode(String province, String city, String code, String isp) {
		super();
		this.province = province;
		this.city = city;
		this.code = code;
		this.isp = isp;
	}

	public Autocode(Integer id, String province, String city, String code, String isp) {
		super();
		this.id = id;
		this.province = province;
		this.city = city;
		this.code = code;
		this.isp = isp;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getProvince() {
		return province;
	}

	public void setProvince(String province) {
		this.province = province;
	}

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
	}

	public String getIsp() {
		return isp;
	}

	public void setIsp(String isp) {
		this.isp = isp;
	}

}
