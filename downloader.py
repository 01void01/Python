import instaloader

# Get instance
loader = instaloader.Instaloader()

# Login using the credentials
# loader.login('_ankit.sharma_01', 'Ankit@80')

# Use Profile class to access metadata of account
profile = instaloader.Profile.from_username(loader.context,'_ankit.sharma_01')
print("Successfully logged in.")

followers = profile.get_posts()

