# Twitter-Data-Analysis

### So here are the bare minimum requirement for completing this task

1. Use this template to create a repository called Twitter-Data-Analysis in your github account. See ["Creating a repository from a template."](https://docs.github.com/en/articles/creating-a-repository-from-a-template) for more information.
2. [Download](https://drive.google.com/drive/folders/19G8dmehf9vU0u6VTKGV-yWsQOn3IvPsd) and extract the necessary data and put it in the data directory. The data should not not be added to git tracking.
3. Create a branch called “bugfix” to fix the bugs in the fix_clean_tweets_dataframe.py and fix_extract_dataframe.py 
4. In branch “bugfix” use the git mv command to rename fix_clean_tweets_dataframe.py to clean_tweets_dataframe.py and fix_extract_dataframe.py  to extract_dataframe.py 
5. Fix the bugs on clean_tweets_dataframe.py and extract_dataframe.py 
6. Multiple times, push the code you are working on to git, and once the fix is complete, merge the fix_bug branch to main branch
7. Create a new branch called “testing” for updating the unit tests in the test/ folder to be applicable to the code you fixed. 
    a. Build your unit and integration tests to run on small data (< 1 MB) that you copied from what is provided - avoid pushing large data to github
    b. Think about the key elements (units can be functions, classes, or modules; multiple of them working together to accomplish a task requires integration testing) of the code base you are working on. Write the following
      - Unit tests: for individual key functions and classes
      - Integration tests: for the integration of multiple units working together
8. After completing the unit and integration tests, merge  the “testing” branch with the main branch
9. In all cases when you merge, make sure you first do Pull Request, review, then accept the merge.
10. Use github actions in your repository such that when you git push new code (or merge a branch) to the main branch, the unit test in tests/*.py runs automatically. All tests should pass.


After Completing this Challenge, you would have explore  

- Unittesting
- Modular Coding
- Software Engineering Best Practices
- Python Package Structure
- Bug Fix (Debugging)

Have Fun and Cheers
