"""
###단위 테스트 목표###
1. check_alarm 메서드가 시작 후 10초가 지나면
  "Alarm!"을 반환하는지 확인
2. check_alarm 메서드가 시작 후 10초가 지나지 않았을 때
  "No alarm yet."을 반환하는지 확인
3. datetime 모듈을 모킹하여 테스트가 실제 시간에 의존하지 않도록 구현
"""

import unittest
from unittest.mock import patch

from Timer import Timer
from datetime import datetime

class TestTimer(unittest.TestCase):
    
    @patch('Timer.datetime')
    def test_check_alarm_Triggered(self, mock_datetime):
        # 시작 시간 설정
        mock_datetime.now.return_value = datetime(2024, 9, 9, 10, 0, 0)
        timer = Timer()

        mock_datetime.now.return_value = datetime(2024, 9, 9, 10, 0, 10)
        result = timer.check_alarm()

        self.assertEqual(result, "Alarm!")

    @patch('Timer.datetime')
    def test_check_alarm_NotTriggered(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 9, 9, 9, 0, 0)
        timer = Timer()

        mock_datetime.now.return_value = datetime(2024, 9, 9, 9, 0, 9)
        result = timer.check_alarm()

        self.assertEqual(result, "No alarm yet.")