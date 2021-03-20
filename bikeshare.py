import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = [
    'all',
    'january',
    'february',
    'march',
    'april',
    'may',
    'june' ]

DAYS_OF_WEEK_DATA = [
    'all',
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday' ]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
#    city = input('Which city you would like to explore? Chicago, New York City or Washington? : ').lower()
#    while city in {'chicago', 'new york city', 'washington'}:
#        print('Please enter valid city and retry!')
#        break

    while True:
        city = input('Which city you would like to explore? Chicago, New York City or Washington? : ').lower()
        if city in {'chicago', 'new york city', 'washington'}:
#            while True:
#                see_header = input('Do you want to see 5 lines of raw data? ').lower()
#                if see_header in {'yes', 'y'}:
#                    df = pd.read_csv(CITY_DATA[city])
#                    print(df.head())
#                else:
#                    break
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month you are interested? Option: all, january, february, ..., june : ').lower()
        if month in MONTH_DATA:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day you would like see? Option: all, monday, tuesday, ..., sunday : ').lower()
        if day in DAYS_OF_WEEK_DATA:
            break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # Add new columns month and day
    df['start time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['start time'].dt.month
    df['day'] = df['start time'].dt.weekday_name

    # Apply filtering to the month and day
    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def ask_view(df):
    """
    Display 5 rows of data if applicable. Continue to show next 5 rows if user enter yes

    Args:
        (str) answer - user input if want to view 5 lines
        (str) start_row - start row index
    """

    start_row = 0
    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            print(df[start_row : start_row+5])
            start_row += 5
        else:
            break


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    print('Most common month is', df['month'].mode()[0])

#    df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d %H:%M:%S')

    # TO DO: display the most common day of week
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.weekday_name
    print('Most common day of week is', df['day_of_week'].mode()[0].title())

    # TO DO: display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    print('Most common start hour is', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station is', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station is', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Station'] = df['Start Station'] + ' to ' + df['End Station']
    print('Most frequent combination of start and end station trip is', df['Start-End Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_hour = df['Trip Duration'].sum() / 3600
    print('Total travel time is', total_travel_hour.round(decimals=2), 'hours')

    # TO DO: display mean travel time
    mean_travel_min = df['Trip Duration'].mean() / 60
    print('The mean travel time is', mean_travel_min.round(decimals=2), 'min')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Count of user types :\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('Counts of gender :\n', df['Gender'].value_counts())
    except KeyError as e:
        print('\nGender information is not available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('\nThe earliest birth year is:', df['Birth Year'].min().astype(int))
        print('The most recent birth year is:', df['Birth Year'].max().astype(int))
        print('The most common birth year is:', df['Birth Year'].mode()[0].astype(int))
        print("\nThis took %s seconds." % (time.time() - start_time))
    except KeyError as e:
        print('Birth Year information is not available.\n')
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        ask_view(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
