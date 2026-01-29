import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _(pd):
    DATA_PATH = "/Users/megankelly/ASDA/housing.csv"

    df = pd.read_csv(DATA_PATH)
    df
    return (df,)


@app.cell
def _():
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.linear_model import Ridge
    return ColumnTransformer, OneHotEncoder, Pipeline, Ridge, StandardScaler


@app.cell
def _(ColumnTransformer, OneHotEncoder, Pipeline, Ridge, StandardScaler, df):
    TARGET = "SalePrice"

    NUM_FEATURES = [
        "GrLivArea",
        "OverallQual",
        "YearBuilt",
        "GarageCars",
        "TotalBsmtSF",
    ]

    CAT_FEATURES = [
        "Neighborhood",
        "HouseStyle",
        "BldgType",
    ]

    FEATURES = NUM_FEATURES + CAT_FEATURES

    X = df[FEATURES]
    y = df[TARGET]

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, NUM_FEATURES),
            ("cat", categorical_transformer, CAT_FEATURES),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", Ridge(alpha=1.0)),
        ]
    )

    model.fit(X, y)
    return NUM_FEATURES, model


@app.cell
def _(df):
    defaults = {
        "GrLivArea": int(df["GrLivArea"].median()),
        "OverallQual": int(df["OverallQual"].median()),
        "YearBuilt": int(df["YearBuilt"].median()),
        "GarageCars": int(df["GarageCars"].median()),
        "TotalBsmtSF": int(df["TotalBsmtSF"].median()),
        "Neighborhood": df["Neighborhood"].mode()[0],
        "HouseStyle": df["HouseStyle"].mode()[0],
        "BldgType": df["BldgType"].mode()[0],
    }

    return (defaults,)


@app.cell
def _(defaults, df, mo):
    gr_liv_area = mo.ui.slider(
        int(df["GrLivArea"].min()),
        int(df["GrLivArea"].max()),
        value=defaults["GrLivArea"],
        step=50,
        label="Living Area (sq ft)",
    )

    overall_qual = mo.ui.slider(
        1,
        10,
        value=defaults["OverallQual"],
        label="Overall Quality (1–10)",
    )

    year_built = mo.ui.slider(
        int(df["YearBuilt"].min()),
        int(df["YearBuilt"].max()),
        value=defaults["YearBuilt"],
        label="Year Built",
    )

    garage_cars = mo.ui.slider(
        0,
        int(df["GarageCars"].max()),
        value=defaults["GarageCars"],
        label="Garage Cars",
    )

    total_bsmt_sf = mo.ui.slider(
        0,
        int(df["TotalBsmtSF"].max()),
        value=defaults["TotalBsmtSF"],
        step=50,
        label="Basement Area (sq ft)",
    )

    neighborhood = mo.ui.dropdown(
        options=sorted(df["Neighborhood"].unique()),
        value=defaults["Neighborhood"],
        label="Neighborhood",
    )

    house_style = mo.ui.dropdown(
        options=sorted(df["HouseStyle"].unique()),
        value=defaults["HouseStyle"],
        label="House Style",
    )

    bldg_type = mo.ui.dropdown(
        options=sorted(df["BldgType"].unique()),
        value=defaults["BldgType"],
        label="Building Type",
    )

    return (
        bldg_type,
        garage_cars,
        gr_liv_area,
        house_style,
        neighborhood,
        overall_qual,
        total_bsmt_sf,
        year_built,
    )


@app.cell
def _(
    bldg_type,
    garage_cars,
    gr_liv_area,
    house_style,
    mo,
    neighborhood,
    overall_qual,
    total_bsmt_sf,
    year_built,
):
    sidebar = mo.vstack(
        [
            mo.md("## 🏠 House Configuration"),
            gr_liv_area,
            overall_qual,
            year_built,
            garage_cars,
            total_bsmt_sf,
            mo.md("### Location & Type"),
            neighborhood,
            house_style,
            bldg_type,
        ],
        gap=1,
    )
    return (sidebar,)


@app.cell
def _(sidebar):
    sidebar

    return


@app.cell
def _(
    bldg_type,
    df,
    garage_cars,
    gr_liv_area,
    house_style,
    model,
    neighborhood,
    overall_qual,
    total_bsmt_sf,
    year_built,
):
    def get_predicted_price_ui():
        import pandas as pd
        import marimo as mo

        # Read current widget values
        input_dict = {
            "GrLivArea": gr_liv_area.value,
            "OverallQual": overall_qual.value,
            "YearBuilt": year_built.value,
            "GarageCars": garage_cars.value,
            "TotalBsmtSF": total_bsmt_sf.value,
            "Neighborhood": neighborhood.value,
            "HouseStyle": house_style.value,
            "BldgType": bldg_type.value,
        }

        input_df = pd.DataFrame([input_dict])
        predicted_price = model.predict(input_df)[0]
        median_price = df["SalePrice"].median()

        # Short labels
        predicted_label = "💰 Predicted Price"
        median_label = "🏠 Median Price"

        # Format values with 2 decimal places
        predicted_value = mo.ui.text(f"${predicted_price:,.2f}")
        median_value = mo.ui.text(f"${median_price:,.2f}")

        # Stack label above value
        predicted_kpi = mo.vstack([mo.ui.text(predicted_label), predicted_value], gap=0.5)
        median_kpi = mo.vstack([mo.ui.text(median_label), median_value], gap=0.5)

        # Place side by side
        return mo.hstack([predicted_kpi, median_kpi], gap=2)

    return (get_predicted_price_ui,)


@app.cell
def _(
    bldg_type,
    garage_cars,
    gr_liv_area,
    house_style,
    neighborhood,
    overall_qual,
    pd,
    total_bsmt_sf,
    year_built,
):
    # inside a new cell
    pd.DataFrame([{
        "GrLivArea": gr_liv_area.value,
        "OverallQual": overall_qual.value,
        "YearBuilt": year_built.value,
        "GarageCars": garage_cars.value,
        "TotalBsmtSF": total_bsmt_sf.value,
        "Neighborhood": neighborhood.value,
        "HouseStyle": house_style.value,
        "BldgType": bldg_type.value,
    }])

    return


@app.cell
def _(
    bldg_type,
    df,
    garage_cars,
    gr_liv_area,
    house_style,
    model,
    neighborhood,
    overall_qual,
    total_bsmt_sf,
    year_built,
):
    import plotly.express as px

    def get_price_distribution():
        import pandas as pd
        import marimo as mo
        import plotly.express as px

        # predicted price
        input_dict = {
            "GrLivArea": gr_liv_area.value,
            "OverallQual": overall_qual.value,
            "YearBuilt": year_built.value,
            "GarageCars": garage_cars.value,
            "TotalBsmtSF": total_bsmt_sf.value,
            "Neighborhood": neighborhood.value,
            "HouseStyle": house_style.value,
            "BldgType": bldg_type.value,
        }
        input_df = pd.DataFrame([input_dict])
        predicted_price = model.predict(input_df)[0]

        # histogram of SalePrice
        fig = px.histogram(
            df, 
            x="SalePrice", 
            nbins=50, 
            title="🏠 Sale Price Distribution",
            opacity=0.7
        )

        # add predicted price vertical line
        fig.add_vline(
            x=predicted_price,
            line_color="red",
            line_dash="dash",
            annotation_text="Predicted Price",
            annotation_position="top right"
        )

        # use plotly in marimo
        return mo.ui.plotly(fig)

    return (get_price_distribution,)


@app.cell
def _(get_price_distribution):
    get_price_distribution()

    return


@app.cell
def _(NUM_FEATURES, model):
    def feature_contribution():
        import pandas as pd
        import marimo as mo
        import plotly.express as px

        # Numeric features and their coefficients
        coef_df = pd.DataFrame({
            "Feature": NUM_FEATURES,
            "Coefficient": model.named_steps['regressor'].coef_[:len(NUM_FEATURES)]
        })

        # Round to 2 decimals
        coef_df["Coefficient"] = coef_df["Coefficient"].round(2)

        # Sort by absolute value and take top 5
        coef_df = coef_df.sort_values(by="Coefficient", key=abs, ascending=False).head(5)

        # Plot
        fig = px.bar(
            coef_df,
            x="Feature",
            y="Coefficient",
            title="📊 Top 5 Feature Contributions (Numeric)",
            text="Coefficient",
        )
        return mo.ui.plotly(fig)

    return (feature_contribution,)


@app.cell
def _(
    bldg_type,
    df,
    garage_cars,
    gr_liv_area,
    house_style,
    model,
    neighborhood,
    overall_qual,
    total_bsmt_sf,
    year_built,
):
    def neighborhood_distribution():
        import pandas as pd
        import marimo as mo
        import plotly.express as px

        # Filter by selected neighborhood
        neighborhood_df = df[df["Neighborhood"] == neighborhood.value]

        # predicted house
        input_df = pd.DataFrame([{
            "GrLivArea": gr_liv_area.value,
            "OverallQual": overall_qual.value,
            "YearBuilt": year_built.value,
            "GarageCars": garage_cars.value,
            "TotalBsmtSF": total_bsmt_sf.value,
            "Neighborhood": neighborhood.value,
            "HouseStyle": house_style.value,
            "BldgType": bldg_type.value,
        }])
        predicted_price = model.predict(input_df)[0]

        fig = px.histogram(
            neighborhood_df,
            x="SalePrice",
            nbins=20,
            title=f"🏘️ Sale Prices in {neighborhood.value}",
            opacity=0.7
        )

        fig.add_vline(
            x=predicted_price,
            line_color="red",
            line_dash="dash",
            annotation_text="Predicted Price",
            annotation_position="top right"
        )

        return mo.ui.plotly(fig)

    return (neighborhood_distribution,)


@app.cell
def _(
    bldg_type,
    df,
    garage_cars,
    gr_liv_area,
    house_style,
    model,
    neighborhood,
    overall_qual,
    total_bsmt_sf,
    year_built,
):
    def living_area_vs_price_clean():
        import pandas as pd
        import plotly.graph_objects as go
        import marimo as mo

        # Predicted house
        input_df = pd.DataFrame([{
            "GrLivArea": gr_liv_area.value,
            "OverallQual": overall_qual.value,
            "YearBuilt": year_built.value,
            "GarageCars": garage_cars.value,
            "TotalBsmtSF": total_bsmt_sf.value,
            "Neighborhood": neighborhood.value,
            "HouseStyle": house_style.value,
            "BldgType": bldg_type.value,
        }])
        predicted_price = model.predict(input_df)[0]
        predicted_gr = input_df["GrLivArea"].iloc[0]

        # Base scatter (actual houses)
        fig = go.Figure()
        fig.add_trace(go.Scattergl(
            x=df["GrLivArea"],
            y=df["SalePrice"],
            mode="markers",
            opacity=0.6,
            marker=dict(size=8, color='blue'),
            name="Actual Houses"
        ))

        # Predicted house as a red star, now visible in legend
        fig.add_trace(go.Scattergl(
            x=[predicted_gr],
            y=[predicted_price],
            mode="markers",
            marker=dict(
                color="red",
                size=16,
                symbol="star",
                line=dict(width=2, color='DarkRed')
            ),
            hovertext=[f"Predicted Price: ${predicted_price:,.0f}"],
            hoverinfo="text",
            showlegend=True,          # show in legend
            name="Predicted House"  # add a star in the legend label if you like
        ))

        # Adjust axes
        x_min = min(df["GrLivArea"].min(), predicted_gr) - 5
        x_max = max(df["GrLivArea"].max(), predicted_gr) + 5
        y_min = min(df["SalePrice"].min(), predicted_price) * 0.95
        y_max = max(df["SalePrice"].max(), predicted_price) * 1.05
        fig.update_xaxes(range=[x_min, x_max])
        fig.update_yaxes(range=[y_min, y_max])

        # Add a title with emoji
        fig.update_layout(
            title="📏 Living Area vs Sale Price",
            hovermode="closest"
        )

        return mo.ui.plotly(fig)

    return (living_area_vs_price_clean,)


@app.cell
def _(
    bldg_type,
    df,
    garage_cars,
    gr_liv_area,
    house_style,
    model,
    neighborhood,
    overall_qual,
    total_bsmt_sf,
    year_built,
):
    def year_built_vs_price_clean():
        import pandas as pd
        import plotly.graph_objects as go
        import marimo as mo

        # Predicted house
        input_df = pd.DataFrame([{
            "GrLivArea": gr_liv_area.value,
            "OverallQual": overall_qual.value,
            "YearBuilt": year_built.value,
            "GarageCars": garage_cars.value,
            "TotalBsmtSF": total_bsmt_sf.value,
            "Neighborhood": neighborhood.value,
            "HouseStyle": house_style.value,
            "BldgType": bldg_type.value,
        }])
        predicted_price = model.predict(input_df)[0]
        predicted_year = input_df["YearBuilt"].iloc[0]

        # Base scatter (actual houses)
        fig = go.Figure()
        fig.add_trace(go.Scattergl(
            x=df["YearBuilt"],
            y=df["SalePrice"],
            mode="markers",
            opacity=0.6,
            marker=dict(size=8, color='blue'),
            name="Actual Houses"
        ))

        # Predicted house as a red star, on top
        fig.add_trace(go.Scattergl(
            x=[predicted_year],
            y=[predicted_price],
            mode="markers",
            marker=dict(
                color="red",
                size=16,
                symbol="star",
                line=dict(width=2, color='DarkRed')  # outline
            ),
            hovertext=[f"Predicted Price: ${predicted_price:,.0f}"],
            hoverinfo="text",
            showlegend=True,
            name="Predicted House"
        ))

        # Adjust axes
        x_min = min(df["YearBuilt"].min(), predicted_year) - 5
        x_max = max(df["YearBuilt"].max(), predicted_year) + 5
        y_min = min(df["SalePrice"].min(), predicted_price) * 0.95
        y_max = max(df["SalePrice"].max(), predicted_price) * 1.05
        fig.update_xaxes(range=[x_min, x_max])
        fig.update_yaxes(range=[y_min, y_max])

        # Add title with emoji
        fig.update_layout(
            title="🏗️ Year Built vs Sale Price",
            hovermode="closest"
        )

        return mo.ui.plotly(fig)

    return (year_built_vs_price_clean,)


@app.cell
def _(get_predicted_price_ui, get_price_distribution, mo, sidebar):
    # Combine sidebar + main panel
    dashboard = mo.hstack(
        [
            sidebar,  # Left column
            mo.vstack(
                [
                    get_predicted_price_ui(),    # KPIs
                    get_price_distribution(),    # Histogram
                ],
                gap=2
            )
        ],
        gap=3
    )

    dashboard


    return (dashboard,)


@app.cell
def _(
    dashboard,
    feature_contribution,
    living_area_vs_price_clean,
    mo,
    neighborhood_distribution,
    year_built_vs_price_clean,
):
    dashboard_full = mo.vstack(
        [
            dashboard,  # existing sidebar + KPIs + main histogram
            mo.hstack([feature_contribution(), neighborhood_distribution()], gap=3),
            mo.hstack([living_area_vs_price_clean(), year_built_vs_price_clean()], gap=3)
        ],
        gap=3
    )

    dashboard_full

    return


if __name__ == "__main__":
    app.run()
