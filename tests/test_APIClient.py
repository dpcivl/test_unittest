"""
###단위 테스트 목표###
1. get_data 메서드가 성공적인 응답(HTTP 200)을 반환했을 때
  올바른 데이터를 반환하는지 확인
2. get_data 메서드가 실패한 응답(HTTP 404, 500)을 처리하고
  적절한 예외를 발생시키는지 확인
"""

import unittest
from unittest.mock import patch

from APIClient import APIClient
import requests

class TestAPIClient(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "Success"}
        
        client = APIClient("http://api.example.com")
        result = client.get_data("test")

        self.assertEqual(result, {"data": "Success"})

    @patch('requests.get')
    def test_get_data_failure(self, mock_get):
        # 가짜 응답 설정 (500 에러)
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

        client = APIClient("http://api.example.com")

        # 예외가 발생하는지 확인
        with self.assertRaises(requests.exceptions.HTTPError):
            client.get_data("test")