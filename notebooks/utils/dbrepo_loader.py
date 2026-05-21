from dbrepo.RestClient import RestClient
import pandas as pd

DATABASE_ID = "be8863ae-9794-4ee2-a964-3e22133b3840"

VIEW_NAMES = {
    "forward": "vw_forward_features",
    "transfer": "vw_transfer_features",
    "combined": "vw_combined_player_value",
    "player_lookup": "vw_player_lookup",
    "club_lookup": "vw_club_lookup",
    "position_lookup": "vw_position_lookup",
    "nationality_lookup": "vw_nationality_lookup",
}


def get_client(
    username='',
    password='',
    base_url="https://test.dbrepo.tuwien.ac.at",
):
    return RestClient(
        base_url=base_url,
        username=username,
        password=password,
    )


def get_view_id_map(
    client,
    database_id=DATABASE_ID,
):
    views = client.get_views(database_id=database_id)

    return {
        view.name: view.id
        for view in views
    }


def fetch_view_df(
    client,
    database_id,
    view_id_map,
    view_name,
):
    try:

        data = client.get_view_data(
            database_id=database_id,
            view_id=view_id_map[view_name],
        )

        df = pd.DataFrame(data)

        print(f"[OK] Retrieved data for: {view_name}")
        print(f"     Shape: {df.shape}")

        return df

    except Exception as e:

        print(f"[WARNING] Could not retrieve data for: {view_name}")
        print(str(e))

        return pd.DataFrame()


def load_lookup_tables(
    client,
    database_id=DATABASE_ID,
):
    view_id_map = get_view_id_map(client, database_id)

    return {
        "player_df": fetch_view_df(client, database_id, view_id_map, VIEW_NAMES["player_lookup"]),
        "club_df": fetch_view_df(client, database_id, view_id_map, VIEW_NAMES["club_lookup"]),
        "position_df": fetch_view_df(client, database_id, view_id_map, VIEW_NAMES["position_lookup"]),
        "nationality_df": fetch_view_df(client, database_id, view_id_map, VIEW_NAMES["nationality_lookup"]),
    }


def load_forward_dataset(
    client,
    database_id=DATABASE_ID,
):
    view_id_map = get_view_id_map(client, database_id)

    forward_df = fetch_view_df(
        client,
        database_id,
        view_id_map,
        VIEW_NAMES["forward"],
    )

    lookups = load_lookup_tables(client, database_id)

    if not forward_df.empty:

        forward_df = forward_df.merge(
            lookups["player_df"],
            on="player_id",
            how="left",
        )

        forward_df = forward_df.merge(
            lookups["club_df"],
            on="club_id",
            how="left",
        )

    return forward_df


def load_transfer_dataset(
    client,
    database_id=DATABASE_ID,
):
    view_id_map = get_view_id_map(client, database_id)

    transfer_df = fetch_view_df(
        client,
        database_id,
        view_id_map,
        VIEW_NAMES["transfer"],
    )

    lookups = load_lookup_tables(client, database_id)

    if not transfer_df.empty:

        transfer_df = transfer_df.merge(
            lookups["player_df"],
            on="player_id",
            how="left",
        )

        transfer_df = transfer_df.merge(
            lookups["club_df"],
            on="club_id",
            how="left",
        )

        transfer_df = transfer_df.merge(
            lookups["position_df"],
            on="position_id",
            how="left",
        )

        transfer_df = transfer_df.merge(
            lookups["nationality_df"],
            on="nationality_id",
            how="left",
        )

    return transfer_df


def load_combined_dataset(
    client,
    database_id=DATABASE_ID,
):
    view_id_map = get_view_id_map(client, database_id)

    combined_df = fetch_view_df(
        client,
        database_id,
        view_id_map,
        VIEW_NAMES["combined"],
    )

    lookups = load_lookup_tables(client, database_id)

    if not combined_df.empty:

        combined_df = combined_df.merge(
            lookups["player_df"],
            on="player_id",
            how="left",
        )

        combined_df = combined_df.merge(
            lookups["club_df"],
            on="club_id",
            how="left",
        )

    return combined_df
