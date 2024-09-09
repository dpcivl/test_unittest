"""
###단위 테스트 목표###
1. write_to_file 메서드가 파일에 데이터를 올바르게 기록하는지 확인
2. read_from_file 메서드가 파일에서 데이터를 올바르게 읽어오는지 확인
3. 실제로 파일을 생성하지 않고 모킹을 사용하여 파일 입출력 동작을 테스트
"""

import unittest
from unittest.mock import mock_open, patch

from FileService import FileService

class TestFileService(unittest.TestCase):
    # open 함수가 호출됐을 때, 실제 파일을 여는 대신 모킹된 mock_open 함수를 사용함
    @patch('builtins.open', new_callable=mock_open)
    def test_write_to_file(self, mock_file):
        file_service = FileService('test.txt')
        file_service.write_to_file('Hello, World')

        # 파일 쓰기 호출 여부 확인
        mock_file.assert_called_once_with('test.txt', 'w')
        mock_file().write.assert_called_once_with('Hello, World')

    @patch('builtins.open', new_callable=mock_open, read_data='Hello, World')
    def test_read_from_file(self, mock_file):
        file_service = FileService('test.txt')
        result = file_service.read_from_file()

        mock_file.assert_called_once_with('test.txt', 'r')
        self.assertEqual(result, 'Hello, World')

    @patch('builtins.open')
    def test_read_from_file_WhenNotExist(self, mock_open):
        # 파일이 없을 때 FileNotFoundError가 발생하도록 설정
        mock_open.side_effect = FileNotFoundError

        file_service = FileService('test.txt')

        # 파일이 없을 때 FileNotFoundError가 발생하는지 확인
        with self.assertRaises(FileNotFoundError):
            file_service.read_from_file()

# mock_open 처음 써봤음