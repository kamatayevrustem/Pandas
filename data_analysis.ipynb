{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "```python\n",
    "count_top3([1880]) == ['John', 'William', 'Mary']\n",
    "count_top3([1900, 1950, 2000]) == ['James', 'John', 'Robert']\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_top3(years_list):\n",
    "    df_list = []\n",
    "    \n",
    "    for year in years_list:\n",
    "        df = pd.read_csv(f'./names/yob{year}.txt', names=['Name', 'Gender', 'Count'])\n",
    "        df_list.append(df)\n",
    "        \n",
    "    new_df = pd.concat(df_list).groupby(['Name']).sum().nlargest(3, 'Count')\n",
    "    \n",
    "    return new_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Name</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>John</th>\n",
       "      <td>9701</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>William</th>\n",
       "      <td>9562</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mary</th>\n",
       "      <td>7092</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Count\n",
       "Name          \n",
       "John      9701\n",
       "William   9562\n",
       "Mary      7092"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count_top3([1880])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Name</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>James</th>\n",
       "      <td>111789</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>John</th>\n",
       "      <td>109601</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Robert</th>\n",
       "      <td>101368</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Count\n",
       "Name          \n",
       "James   111789\n",
       "John    109601\n",
       "Robert  101368"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count_top3([1900, 1950, 2000])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "```python\n",
    "count_dynamics([1900, 1950, 2000]) == {\n",
    "  'F': [299810, 1713259, 1814922],\n",
    "  'M': [150486, 1790871, 1962744]\n",
    "}\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def count_dynamics(years_list):\n",
    "    data = pd.DataFrame()\n",
    "    \n",
    "    for year in years_list:\n",
    "        df = pd.read_csv(f'./names/yob{year}.txt', names=['Name', 'Gender', 'Count'])\n",
    "        df['Year'] = year\n",
    "        data = pd.concat([data, df])\n",
    "        \n",
    "    return data.groupby(['Gender', 'Year']).sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>Count</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <th>Year</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">F</th>\n",
       "      <th>1900</th>\n",
       "      <td>299798</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1950</th>\n",
       "      <td>1713065</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2000</th>\n",
       "      <td>1815295</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"3\" valign=\"top\">M</th>\n",
       "      <th>1900</th>\n",
       "      <td>150480</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1950</th>\n",
       "      <td>1790437</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2000</th>\n",
       "      <td>1963202</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Count\n",
       "Gender Year         \n",
       "F      1900   299798\n",
       "       1950  1713065\n",
       "       2000  1815295\n",
       "M      1900   150480\n",
       "       1950  1790437\n",
       "       2000  1963202"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "count_dynamics([1900, 1950, 2000])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
