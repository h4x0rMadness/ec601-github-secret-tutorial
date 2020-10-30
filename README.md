# Tutorial: How to separate your API keys from your scripts using Github Secrets

This is a tutorial to solve the problem that your script may need to contain your valuable API keys and secrets.

For more information, you can check out the `twitter_example.py`, `test_twitter_example.py` and `Github Workflow file` in this repository.
Also, check this github documentation for [Github Secrets](https://docs.github.com/cn/free-pro-team@latest/actions/reference/encrypted-secrets)

## Step 1

-   Go to the `repository `where you want to separate your keys from the script
-   Go to `Settings `-> `Secrets`, select `New secret`, name it something like `ACCESS_TOKEN` `CONSUMER_KEY` or any name that makes sense to you (no name starts with `Github_` is allowed here). But I recommend that you use the same name, so that no confusion in the future steps.
-   Also input the values here, **NO QUOTATION MARKS needed**, if you do include them, it won’t work!!
-   Repeat and create all the keys, secrets you need for your project (for my very simple Twitter script, I need four secrets as shown in the following picture)![pic1](https://github.com/h4x0rMadness/ec601-github-secret-tutorial/blob/main/pics/1.png)



So far, you have set up the keys in this repo, and you don’t have to worry about getting your keys leaked by forking this repo or something, it’s safe (says `Github`)



## Step 2

-   I assume you are using `Github Actions` as required

-   Go to your `Github`-> `Actions`, find your `Workflow file` (which ends up with `.yml`)

-   Before running `pytest`, you should add lines like this:

    ```yaml
    env:
              CONSUMER_KEY: ${{ secrets.CONSUMER_KEY }}
              CONSUMER_SECRET:  ${{ secrets.CONSUMER_SECRET }} 
              ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
              ACCESS_TOKEN_SECRET: ${{ secrets.ACCESS_TOKEN_SECRET }}     
    ```

    For example, my `.yml` file was like this before modification:

    ![image-20201030133617289](https://github.com/h4x0rMadness/ec601-github-secret-tutorial/blob/main/pics/2.png)

    And after modification, it looks like this:

    ![image-20201030133702416](https://github.com/h4x0rMadness/ec601-github-secret-tutorial/blob/main/pics/3.png)

    notice here, the name after `secrets.` in the `secrets.CONSUMER_KEY` should be whatever set up in the last step in your `Github Secrets`

-   Do the same replacement if you have different `Secret `names

-   The purpose of this step is to set up `environment variables` in the virtual environment in` Github Actions`.

## Step 3

-   Go to your python script / python unit test file which contains Twitter keys
-   Now you can assume the environment variables contain the keys you need for fetching data from Twitter (as you just set up in `Github Secrets` and `Github Actions`, well done!)
-   Therefore, you should not have any **ACTUAL** keys or secrets in your scripts, instead, you should use something like:

```python
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        
        ## you need to `import os` for this operation
```

-   By doing this, you protect your keys and secrets while your repo can still be public




