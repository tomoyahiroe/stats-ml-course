import requests
import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# APIのエンドポイントからCSVデータを取得し，データフレームを作成する関数
def get_csv_request(endpoint: str):
    text = requests.get(endpoint).text
    file_like_object = io.StringIO(text)
    df = pd.read_csv(file_like_object)
    return df


# データの取得
base_url = 'https://raw.githubusercontent.com/TaddyLab/BDS/refs/heads/master/examples/'
trucks_url = base_url + 'pickup.csv'
trucks = get_csv_request(trucks_url)


# 箱ひげ図のプロット
plt.style.use('ggplot')
fig_box = plt.figure()
ax_box = fig_box.add_subplot(111)
sns.boxplot(data=trucks, x="make", y="price", ax=ax_box)
fig_box.savefig('boxplot.png')


# ヒストグラムのプロット
fig_hist = plt.figure()
ax_hist = fig_hist.add_subplot(111)
sns.histplot(data=trucks, x="price", bins=5,
             binrange=(0, 25000), ax=ax_hist)
ax_hist.set_ylabel("frequency")
fig_hist.savefig('histogram.png')


# 散布図のプロット
fig_scatter = plt.figure()
ax_scatter = fig_scatter.add_subplot(111)
sns.scatterplot(data=trucks, x="year", y="price", hue="make", ax=ax_scatter)
fig_scatter.savefig('scatterplot.png')


# オンライン支出のデータを取得
browser_url = base_url + 'web-browsers.csv'
browser = get_csv_request(browser_url)
# print(browser.columns)


# 年間オンライン支出のヒストグラム
fig_browser = plt.figure()
ax_browser = fig_browser.add_subplot(111)
ax_browser.set_xscale('log')
sns.histplot(data=browser, x="spend", bins=12)
ax_browser.set_xlabel("total online spend")
ax_browser.set_ylabel("density")
fig_browser.savefig('density.png')


# 課題３
path = "/Users/hiroetomokana/.cache/kagglehub/datasets/nikhil25803/github-dataset/versions/2"

repositories = pd.read_csv(f"{path}/repository_data.csv")

selected_language = ["Go", "Rust", "C++"]
repositories = repositories.loc[repositories["primary_language"].isin(
    selected_language)]
repositories["created_at"] = pd.to_datetime(repositories["created_at"])


plt.style.use('ggplot')
fig_github = plt.figure()  # 描画範囲の作成

ax_box_github = fig_github.add_subplot(222)  # 箱ひげ図のプロット
sns.boxplot(data=repositories, x="primary_language",
            y="stars_count", ax=ax_box_github, showfliers=False)

ax_hist_github = fig_github.add_subplot(223)  # ヒストグラム
sns.histplot(data=repositories, x="stars_count", bins=10000, ax=ax_hist_github)
ax_hist_github.set_ylabel("frequency")

ax_scatter_github = fig_github.add_subplot(224)  # 散布図のプロット
sns.scatterplot(data=repositories, x="created_at",
                y="stars_count", hue="primary_language", ax=ax_scatter_github)
fig_github.savefig("github.png")
