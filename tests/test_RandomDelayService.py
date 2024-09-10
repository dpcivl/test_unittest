"""
###단위 테스트 목표###
1. 랜덤 지연 시간이 발생하는지 확인하고,
  이 지연 시간을 Mock하여 제어
2. call_service 메서드가 지연 후 정상적으로 실행되는지 확인
3. 시간 지연이 실제로 발생하지 않도록 Mock을 사용하여 테스트 실행 시간을 줄임
"""

import unittest
from unittest.mock import patch

from RandomDelayService import RandomDelayService

class TestRandomDelayService(unittest.TestCase):
    @patch('RandomDelayService.random.uniform')
    @patch('RandomDelayService.time.sleep')
    def test_call_service(self, mock_sleep, mock_uniform):
        mock_uniform.return_value = 3.0

        service = RandomDelayService()
        result = service.call_service()

        # 1~5 범위로 호출되었는지 확인
        mock_uniform.assert_called_once_with(1, 5)

        mock_sleep.assert_called_once_with(3.0)

        self.assertEqual(result, "Service called after delay")

# 2개 이상의 patch를 필요로 할 땐, 각 줄에 선언