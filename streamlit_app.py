# app.py
import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
from folium.plugins import MarkerCluster

st.set_page_config(page_title="Santa Cruz Eats", layout="wide", page_icon="🍴")

# ---- Minimal CSS for nicer look ----
st.markdown(
    """
    <style>
    .header {
        display:flex;
        justify-content:space-between;
        align-items:center;
        gap:10px;
    }
    .hero {
        background: linear-gradient(90deg, rgba(255,140,0,0.06), rgba(255,69,0,0.02));
        border-radius:12px;
        padding:18px;
    }
    .place-card {
        border-radius:10px;
        padding:10px;
    }
    .small-muted { color: #6c757d; font-size:0.9rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- Sample dataset: replace or extend with your own data ----
PLACES = [
    {
        "id": "picnic_basket",
        "name": "The Picnic Basket",
        "lat": 36.9628,
        "lon": -122.0208,
        "desc": "Beachfront cafe serving seasonal breakfasts, sandwiches, and locally-sourced ingredients. Great for seaside views and casual outdoor dining.",
        "hours": "Daily 8:00 AM - 4:00 PM. Best at sunrise or sunset for views.",
        "price": "$$ (around $10–25 per person)",
        "tags": ["beachfront", "cafe", "sandwiches"],
        "images": [
            "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1200&q=60"
        ],
    },
    {
        "id": "seabreeze_cafe",
        "name": "Seabreeze Cafe",
        "lat": 36.9620,
        "lon": -121.9449,
        "desc": "Local favorite for hearty breakfasts and vegan-friendly options; expect a line on weekends.",
        "hours": "Tue-Sun 7:30 AM - 2:00 PM (closed Wed).",
        "price": "$ (around $8–15 per person)",
        "tags": ["breakfast", "local", "vegan"],
        "images": [
            "https://images.unsplash.com/photo-1504754524776-8f4f37790ca0?auto=format&fit=crop&w=1200&q=60"
        ],
    },
    {
        "id": "jack_oneill",
        "name": "Jack O'Neill Restaurant",
        "lat": 36.9629,
        "lon": -122.0166,
        "desc": "Upscale coastal dining with ocean views and an emphasis on local seafood. Ideal for special occasions or sunset dinners.",
        "hours": "Daily 11:30 AM - 9:00 PM.",
        "price": "$$$ (around $35+ per person)",
        "tags": ["oceanview", "seafood", "upscale"],
        "images": [
            "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1200&q=60"
        ],
    },
    {
        "id": "truck_stop_sc",
        "name": "The Truck Stop (Food Truck)",
        "lat": 36.9662,
        "lon": -122.0235,
        "desc": "A rotating lineup of food trucks offering tacos, gourmet sandwiches, and fusion street food. Check the schedule for weekly vendors.",
        "hours": "Fri evenings (seasonal events) and special pop-ups.",
        "price": "$ (around $6–12 per dish)",
        "tags": ["food_truck", "casual", "street_food"],
        "images": [
            "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=1200&q=60"
        ],
    },
    {
        "id": "seabright_deli",
        "name": "Seabright Deli",
        "lat": 36.9615,
        "lon": -121.9420,
        "desc": "Classic deli with house-smoked meats, large sandwiches and salads. Good for takeout and dog-friendly outdoor seating.",
        "hours": "Tue-Sun 11:00 AM - 4:00 PM.",
        "price": "$$ (around $12–18 per person)",
        "tags": ["deli", "takeout", "local"],
        "images": [
            "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=1200&q=60"
        ],
    },
]

# Convert to DataFrame for convenient lookups
df_places = pd.DataFrame(PLACES).set_index("id")


# ---- Helper functions ----
def build_map(place_df, center=(36.9628, -122.0208), zoom_start=13):
    m = folium.Map(location=center, zoom_start=zoom_start, tiles="CartoDB positron")
    marker_cluster = MarkerCluster().add_to(m)

    for pid, r in place_df.iterrows():
        folium.Marker(
            location=(r["lat"], r["lon"]),
            popup=folium.Popup(f"<b>{r['name']}</b><br/>{r['desc'][:120]}...", max_width=300),
            tooltip=r["name"],
            icon=folium.Icon(color="red", icon="cutlery", prefix="fa"),
            # store id in the folium element so we can detect clicks (last_object_clicked)
        ).add_to(marker_cluster)
    return m


def recommend_similar(selected_tags, all_places, top_n=3):
    """Simple recommendation: score by shared tags"""
    scores = []
    for pid, p in all_places.iterrows():
        tags = p["tags"]
        if isinstance(tags, str):
            tags = eval(tags)
        shared = len(set(selected_tags) & set(tags))
        scores.append((pid, shared))
    # sort by score desc and exclude exact match if exists
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return [s[0] for s in scores if s[1] > 0][:top_n]


# ---- Sidebar: navigation ----
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Gallery", "Map", "About"])

# ---- Top header (hero) ----
if page == "Home":
    st.markdown(
        """
        <div class="header hero">
            <div>
                <h1 style="margin:0">Santa Cruz Eats 🍴</h1>
                <p class="small-muted">A friendly guide to cafes, restaurants, and food trucks across Santa Cruz.</p>
            </div>
            <div style="text-align:right">
                <p style="margin:0">Discover seaside cafes • Find local favorites • Plan your visit</p>
                <a href="#map" style="font-weight:500">Jump to map ↓</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Food destinations for every mood")
        st.write(
            """
            Whether you want a coffee with an ocean view, a quick fish taco, or a relaxed brunch spot,
            Santa Cruz has delightful eats around every corner. Use the interactive map to explore locations,
            browse the gallery for inspiring photos, and tap a place to see details and recommendations.
            """
        )
        # Quick highlights cards
        with st.container():
            c1, c2, c3 = st.columns(3)
            c1.markdown("**Beachfront views**\n\nDine on the sand or watch the sunset.")
            c2.markdown("**Local favorites**\n\nSmall, family-run places with character.")
            c3.markdown("**Food trucks & popups**\n\nSeasonal, fun, and great for groups.")
    with col2:
        # Small gallery preview
        imgs = [p["images"][0] for p in PLACES[:3]]
        for url in imgs:
            st.image(url, use_column_width=True)

    st.markdown("---")
    st.subheader("Featured on the Map")
    folium_map = build_map(df_places)
    # display in wide area
    map_data = st_folium(folium_map, width=900, height=400)

    st.markdown("### Quick pick")
    columns = st.columns(3)
    for col, place in zip(columns, PLACES[:3]):
        col.markdown(f"**{place['name']}**")
        col.markdown(place["desc"][:120] + "...")
        col.markdown(f"<span class='small-muted'>{place['price']}</span>", unsafe_allow_html=True)

elif page == "Gallery":
    st.header("Image Gallery — Santa Cruz Food & Eats")
    st.write("Browse photos of restaurants, cafes, and food trucks. Click any image to expand.")

    # grid of images
    rows = 2
    per_row = 3
    idx = 0
    for r in range(rows):
        cols = st.columns(per_row)
        for c in cols:
            if idx < len(PLACES):
                p = PLACES[idx]
                c.image(p["images"][0], caption=p["name"], use_column_width=True)
                idx += 1

    st.markdown("---")
    st.subheader("Filter by tag")
    # simple filter
    all_tags = sorted({t for p in PLACES for t in p["tags"]})
    chosen = st.multiselect("Select tags to filter", all_tags, default=[])
    filtered = [p for p in PLACES if (set(chosen) <= set(p["tags"]) if chosen else True)]
    st.write(f"Showing {len(filtered)} places")
    cols = st.columns(3)
    for i, p in enumerate(filtered):
        cols[i % 3].image(p["images"][0], caption=f"{p['name']} — {p['price']}", use_column_width=True)

elif page == "Map":
    st.header("Interactive Map — Explore Places")
    st.write("Click markers to see a brief popup. Use the list below to select a place for more details.")

    # Build and show map
    center = (df_places["lat"].mean(), df_places["lon"].mean())
    m = build_map(df_places, center=center)
    map_result = st_folium(m, height=600, width="100%")

    # Map returns various keys, look for clicked object
    clicked = map_result.get("last_object_clicked") or map_result.get("last_clicked")
    # To allow selection by list
    st.markdown("### Or pick from the list")
    selected_name = st.selectbox("Choose a place", ["-- choose --"] + [p["name"] for p in PLACES])
    selected_id = None
    if selected_name and selected_name != "-- choose --":
        # find id
        for p in PLACES:
            if p["name"] == selected_name:
                selected_id = p["id"]
                break

    # If user clicked a marker, try to infer which place is closest (approx)
    if clicked and not selected_id:
        # clicked may be a dict with 'lat' and 'lng', try to read
        try:
            lat = clicked.get("lat") or clicked.get("latitude")
            lon = clicked.get("lng") or clicked.get("longitude")
            if lat and lon:
                # find nearest place
                distances = [
                    (p["id"], (p["lat"] - lat) ** 2 + (p["lon"] - lon) ** 2) for p in PLACES
                ]
                distances.sort(key=lambda x: x[1])
                selected_id = distances[0][0]
        except Exception:
            selected_id = None

    if selected_id:
        p = df_places.loc[selected_id]
        st.markdown("---")
        st.markdown(f"## {p['name']}")
        c1, c2 = st.columns([2, 1])
        with c1:
            st.write(p["desc"])
            st.write("**Best times to visit:**", p["hours"])
            st.write("**Cost info:**", p["price"])
            st.markdown("**Tags:** " + ", ".join(p["tags"]))
            st.markdown("### Recommendations")
            rec_ids = recommend_similar(p["tags"], df_places)
            if rec_ids:
                for rid in rec_ids:
                    if rid == selected_id:
                        continue
                    rp = df_places.loc[rid]
                    st.markdown(f"- **{rp['name']}** — {rp['desc'][:120]}...")
            else:
                st.write("No similar places found.")
        with c2:
            # show images
            imgs = p["images"]
            for url in imgs:
                st.image(url, use_column_width=True)
    else:
        st.info("Click a marker on the map or choose a place from the list to see details.")

elif page == "About":
    st.header("About this blog")
    st.write(
        """
        This Streamlit app is a small interactive guide to eating in Santa Cruz.
        It demonstrates:
        - a clean landing page,
        - an image gallery,
        - an interactive Folium map (click markers),
        - detail pages with recommendations.

        You can extend it by:
        - adding more places to the PLACES list,
        - connecting to a backend or Google Sheets for live updates,
        - user ratings and comments (requires auth/storage),
        - improved responsive styling and image hosting.
        """
    )
    st.markdown("---")
    st.markdown("**Data & images:**")
    st.write("Sample images used for illustration were taken from public image resources and place webpages for Santa Cruz venues. Replace them with your own high-resolution photos for production. ")

# ---- Footer / small note ----
st.markdown(
    """
    <div style="padding:10px; text-align:center; color:#6c757d;">
    Built with Streamlit • Replace sample data with your own to personalize the blog.
    </div>
    """,
    unsafe_allow_html=True,
)
