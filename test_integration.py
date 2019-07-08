#!/usr/bin/env python

"""
Author: Nick Russo
Purpose: Using pytest for simple integration testing to
interact with dockerized web servers within a CI/CD pipeline.
"""

import requests


# consider reversing ACCT100 to make the number be 40 to
# prevent more wireshark captures


def test_get_page():
    """
    Simulate a user navigating to the website with an HTTP GET.
    """
    get_headers = {"Accept": "text/html"}
    for port in [5001, 5002, 5003]:
        resp = requests.get(f"http://localhost:{port}", headers=get_headers)
        assert resp.status_code == 200
        assert "Enter account ID" in resp.text


def test_post_good_acct():
    """
    Simulate a user entering an account number and clicking "Submit".
    """
    data = "acctid=ACCT100"
    post_headers = {
        "Accept": "text/html",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    for port in [5001, 5002, 5003]:
        resp = requests.post(
            f"http://localhost:{port}", headers=post_headers, data=data
        )
        assert resp.status_code == 200
        assert "Account balance: -40" in resp.text


def test_post_good_acct():
    """
    Simulate a user entering a valid account number and clicking "Submit".
    """
    _post_acct({"acctid": "ACCT100", "acctbal": -40})


def test_post_bad_acct():
    """
    Simulate a user entering an invalid account number and clicking "Submit".
    """
    _post_acct({"acctid": "bogus123"})


def _post_acct(acct):
    post_headers = {
        "Accept": "text/html",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    for port in [5001, 5002, 5003]:
        resp = requests.post(
            f"http://localhost:{port}",
            headers=post_headers,
            data=f"acctid={acct['acctid']}",
        )
        assert resp.status_code == 200
        balance = acct.get("acctbal")
        if balance:
            assert f"Account balance: {balance}" in resp.text
        else:
            assert "Unknown account number" in resp.text
