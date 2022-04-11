SQL = sudo mysql -u root -p

t0:
	mv task_test_files/0-select_states.sql .
	cat 0-select_states.sql | $(SQL)
	mv 0-select_states.sql task_test_files

t4:
	mv task_test_files/4-cities_by_state.sql .
	cat 4-cities_by_state.sql | $(SQL)
	mv 4-cities_by_state.sql task_test_files

t6:
	mv task_test_files/6-model_state.sql .
	cat 6-model_state.sql | $(SQL)
	mv 6-model_state.sql task_test_files

t7:
	mv task_test_files/7-model_state_fetch_all.sql .
	cat 7-model_state_fetch_all.sql | $(SQL)
	mv 7-model_state_fetch_all.sql task_test_files

t14:
	mv task_test_files/14-model_city_fetch_by_state.sql .
	cat 14-model_city_fetch_by_state.sql | $(SQL)
	mv 14-model_city_fetch_by_state.sql task_test_files
