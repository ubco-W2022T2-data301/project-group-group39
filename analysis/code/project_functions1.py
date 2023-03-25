import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def load_and_process(url_or_path_to_csv_file):
    
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .drop(columns=[col for col in df.columns if col not in ["ts_pct", "pts", "player_name", "season"]])
        .rename(columns={"ts_pct": "overall_pct"})
        .dropna()
    )

    
    players = ["Stephen Curry", "Giannis Antetokounmpo", "Luka Doncic", "Kevin Durant", "Nikola Jokic", "Joel Embiid", "LeBron James",'James Harden', 'Trae Young','Jayson Tatum']
    player_stats = (
        df1[df1["player_name"].isin(players)][["player_name", "pts", "gp"]]
        .assign(true_total_pts=lambda x: x["pts"] * x["gp"])
        .groupby("player_name")
        .agg({"true_total_pts": "sum"})
        .reset_index()
    )

    return player_stats

