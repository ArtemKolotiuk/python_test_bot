from api_tests import test_create_user, test_create_user_invalid_data, test_get_users


if __name__ == '__main__':
	test_create_user()
	test_create_user_invalid_data()
	test_get_users()