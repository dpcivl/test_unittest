"""
###단위 테스트 목표###
1. save_data 메서드가 데이터베이스에 데이터를 올바르게 저장하는지 테스트
2. get_data 메서드가 데이터베이스에서 데이터를 올바르게 조회하는지 테스트
3. 실제 데이터베이스 연결 없이 모킹을 통해 데이터베이스 동작을 시뮬레이션
4. 커밋과 커서 작업이 적절하게 호출되었는지 확인
"""
import unittest
from unittest.mock import Mock

from DatabaseService import DatabaseService

class TestDatabaseService(unittest.TestCase):
    
    def setUp(self):
        self.mock_db_connection = Mock()
        self.mock_cursor = Mock()
        self.mock_db_connection.cursor.return_value = self.mock_cursor

        self.service = DatabaseService(self.mock_db_connection)

    def test_save_data(self):
        result = self.service.save_data("test_data")
        # 내부에서 cursor.execute 실행
        # db_connection.commit() 한 번 수행

        self.mock_cursor.execute.assert_called_once_with(
            "INSERT INTO data_table (data) VALUES (%s)", ("test_data",)
        )

        self.mock_db_connection.commit.assert_called_once()

        self.assertTrue(result)

    def test_get_data(self):
        self.mock_cursor.fetchone.return_value = ("test_data",)

        result = self.service.get_data(1)

        self.mock_cursor.execute.assert_called_once_with(
            "SELECT data FROM data_table WHERE id = %s", (1,)
        )

        self.assertEqual(result, "test_data")