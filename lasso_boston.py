import os
from pathlib import Path


try:
    import pandas as pd
    from sklearn.linear_model import LassoCV
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
except ModuleNotFoundError as error:
    missing_name = error.name
    raise SystemExit(
        f"{missing_name} が見つかりません。\n"
        "先に次のコマンドで必要なライブラリを入れてください:\n"
        "python3 -m pip install pandas scikit-learn"
    ) from error


CSV_PATH = Path(os.environ.get("BOSTON_CSV_PATH", "data/boston.csv"))
TARGET_COLUMN = "MEDV"


def main():
    if not CSV_PATH.exists():
        raise SystemExit(
            f"{CSV_PATH} が見つかりません。\n"
            "boston.csv を data フォルダに入れるか、BOSTON_CSV_PATH にCSVの場所を指定してください。"
        )

    # データを読み込む。先頭列は sample_1 などの名前なので index として扱う。
    df = pd.read_csv(CSV_PATH, index_col=0)

    # 目的変数 y と説明変数 X に分ける。
    y = df[TARGET_COLUMN]
    X = df.drop(columns=[TARGET_COLUMN])

    # 学習用データとテスト用データに分ける。
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=0,
    )

    # Lasso は変数のスケールに影響されやすいので、標準化してから学習する。
    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("lasso", LassoCV(cv=5, random_state=0, max_iter=10000)),
        ]
    )
    model.fit(X_train, y_train)

    # テスト用データで予測し、モデルの精度を確認する。
    y_pred = model.predict(X_test)
    print("R2:", r2_score(y_test, y_pred))
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("選ばれた alpha:", model.named_steps["lasso"].alpha_)

    # 係数を確認する。0 に近い説明変数ほど、Lasso によって影響が小さいと判断された。
    coef = pd.Series(model.named_steps["lasso"].coef_, index=X.columns)
    print("\n係数:")
    print(coef.sort_values(key=abs, ascending=False))

    # 実測値と予測値を並べて確認する。
    result = pd.DataFrame(
        {
            "実測値": y_test,
            "予測値": y_pred,
            "誤差": y_test - y_pred,
        }
    )
    print("\n予測結果:")
    print(result.head(10))


if __name__ == "__main__":
    main()
