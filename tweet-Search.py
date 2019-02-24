import yaml

creds ="""
    search_tweets_premium:
        account_type: premium
        endpoint: please enter endpoint
        bearer_token: please enter bearer token
    """

# Save the credentials to YAML file

with open('search_tweets_creds.yaml', 'w') as outfile:
    yaml.dump(creds, outfile, default_flow_style=False)



# Load credentials 

from searchtweets import ResultStream, gen_rule_payload, load_credentials


# Enter your keys/secrets as strings in the following fields if no YAML file
SEARCHTWEETS_ENDPOINT = 'Please enter endpoint'
SEARCHTWEETS_BEARER_TOKEN = 'Please enter Bearer Token'
SEARCHTWEETS_ACCOUNT_TYPE = 'premium'
SEARCHTWEETS_CONSUMER_KEY = 'Please enter consumer key'
SEARCHTWEETS_CONSUMER_SECRET = 'Please enter consumer secret'

premium_search_args = load_credentials(filename='search_tweets_creds.yaml',              
                                        yaml_key='search_tweets_premium',
                                        env_overwrite=False)



#Rule for twitter search

rule = gen_rule_payload("keyword", results_per_call=100)  
print(rule)

from searchtweets import collect_results


tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=premium_search_args)
[print(tweet.all_text) for tweet in tweets[0:10]];

#Structure data into the data frames
import pandas
df = df = pd.DataFrame(tweets) 
df.to_csv('file.csv') 