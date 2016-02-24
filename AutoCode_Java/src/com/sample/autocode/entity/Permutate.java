package com.sample.autocode.entity;

import java.io.Serializable;

public class Permutate implements Serializable {

	private Integer id;
	private String tail;

	public Permutate() {

	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getTail() {
		return tail;
	}

	public void setTail(String tail) {
		this.tail = tail;
	}

	public Permutate(Integer id, String tail) {
		super();
		this.id = id;
		this.tail = tail;
	}

	public Permutate(String tail) {
		super();
		this.tail = tail;
	}

}
