"""
###단위 테스트 목표###
1. add_user 메서드가 새로운 사용자를 저장하고, 
  중복된 사용자 ID가 있으면 ValueError를 발생시키는지 확인
2. get_user 메서드가 사용자 정보를 올바르게 반환하는지 확인
3. 데이터베이스 의존성을 모킹하여 테스트가 외부 시스템에 의존하지 않도록 구현 
"""

import unittest
from unittest.mock import Mock

from UserRepository import UserRepository

class TestUserRepository(unittest.TestCase):
    
    def setUp(self):
        self.mock_db = Mock()
        self.user_repo = UserRepository(self.mock_db)

    def test_add_user(self):
        self.mock_db.get.return_value = None

        self.user_repo.add_user(1, "Alice")

        self.mock_db.save.assert_called_once_with(1, "Alice")

    def test_add_user_ValueError(self):
        self.mock_db.get.return_value = "Alice"

        with self.assertRaises(ValueError):
            self.user_repo.add_user(1, "Alice")

    def test_get_user(self):
        self.mock_db.get.return_value = "Alice"

        user = self.user_repo.get_user(1)

        self.assertEqual(user, "Alice")
