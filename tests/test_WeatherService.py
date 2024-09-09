"""
###단위 테스트 목표###
1. get_weather 메서드가 정상적으로 날씨 데이터를 반환하는지 확인
2. get_weather 메서드가 API 호출 실패 시 적절한 예외를 발생시키는지 확인
3. 외부 API 호출을 모킹하여 테스트가 외부 의존성 없이 실행되도록 구현

- unittest의 mock 기능을 사용하여 requests.get 호출을 모킹
- get_weather 메서드가 정상적으로 데이터를 반환하는지 확인하는 테스트 코드 작성
- requests.get이 실패하는 경우(예:500 응답 코드)에 예외가 발생하는지 확인하는 테스트 코드를 작성
"""
import unittest
from unittest.mock import patch

from WeatherService import WeatherService

class TestWeatherService(unittest.TestCase):

    # 모킹 어떻게 적용하는지 모름
    @patch('requests.get')
    def test_get_weather(self, mock_get):
        # 정상적으로 날씨 반환
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "current": {
                "temperature": 25
            }
        }

        weather_service = WeatherService("dummy_api_key")
        temp = weather_service.get_weather("Seoul")

        self.assertEqual(temp, 25)

    @patch('requests.get')
    def test_get_weather_WhenFailToCallAPI(self, mock_get):
        # API 호출 실패 시 적절한 예외를 발생시키는지
        mock_get.return_value.status_code = 500

        weather_service = WeatherService("dummy_api_key")

        with self.assertRaises(Exception):
            weather_service.get_weather("Seoul")