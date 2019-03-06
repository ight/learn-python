from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
  # check that we get a 404 on the url /
  resp = app.request("/")
  assert_response(resp, status="404")

  # test /hello
  resp = app.request("/hello")
  assert_response(resp)

  # check the default value of the form
  resp = app.request("/hello", metho="POST")
  assert_response(resp, contains="Nobody")

  # test when value passed in form
  data = ['name': 'Zed', 'greet': 'Hola']
  resp = app.request("/hello", metho="POST", data=data)
  assert_response(resp, contains="Zed")