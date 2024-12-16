def pytest_collection_finish(session):
    long_tests_count = 0
    quick_tests_count = 0
    for item in session.items:
        if item.get_closest_marker('long_running'):
            long_tests_count += 1
        else:
            quick_tests_count += 1
    print("Collected quick tests: {}, long-running tests: {}".format(quick_tests_count, long_tests_count))

