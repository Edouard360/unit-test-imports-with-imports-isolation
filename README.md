# unit-test-imports-with-imports-isolation
Unit test imports, with imports isolation

Linked to StackOverflow issue:

I have a python package that uses dev and prod libraries.
I want to make sure that some files in that packages never import any dev libraries, as these files are used for deployment
and should only import prod libraries.

For instance, I would want to have a unit tests that fails with that `my_package.__init__.py` but succeeds if we remove the dev library import.

https://github.com/Edouard360/unit-test-imports-with-imports-isolation/blob/7ddecbfa1df8ff308fce0acbfffb131c78c00feb/my_package/__init__.py#L1-L2
 
<img src="https://user-images.githubusercontent.com/15527397/111035109-798a0980-83de-11eb-8d95-756d290107d2.png" width="500">

It's easy to make a **independent test** that satifies those conditions, and expectedly fails on the dev imports  `my_package.__init__.py` while succeeding otherwise:

https://github.com/Edouard360/unit-test-imports-with-imports-isolation/blob/7ddecbfa1df8ff308fce0acbfffb131c78c00feb/unit_tests/test_my_package_imports.py#L6-L10

However, when running the full unit tests suite, for instance with `pytest`, the tests can fail.
This happens if there is another unit test in the same suite that runs some tests against the dev library, for instance:

https://github.com/Edouard360/unit-test-imports-with-imports-isolation/blob/7ddecbfa1df8ff308fce0acbfffb131c78c00feb/unit_tests/test_dev_script.py#L5-L7

Ideally, I would like both tests to be able to coexist in the same `unit_tests` directory, but it seems like imports
are all loaded together at the beginning of all tests. I was wondering if there was a way to isolate that.
I've seen a few related issues that mock the `sys.module` object but I still end up with the same conclusions:
Running independently the test works fine, but not running is at the test suite level 
