import os, sys, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("USDA_API_KEY")
if not API_KEY:
    raise SystemExit("Set USDA_API_KEY environment variable first.")
SEARCH_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

def search_foods(query, page_size=25):
    r = requests.get(SEARCH_URL, params={
        "api_key": API_KEY,
        "query": query,
        "pageSize": page_size
    }, timeout=10)
    # sends a web request to the usda url, and stores result into obj r.

    r.raise_for_status()
    return r.json().get("foods", [])

def get_nutrient(food, name):
    for n in food.get("foodNutrients", []):
        if n.get("nutrientName") == name:
            return n.get("value")
    return None

def simple_search(query):
    foods = search_foods(query, page_size=10)   # r.json().get("foods", [])
    if not foods:
        print("No results.")
        return
    for f in foods:
        kcal = get_nutrient(f, "Energy")
        prot = get_nutrient(f, "Protein")
        fat  = get_nutrient(f, "Total lipid (fat)")
        carb = get_nutrient(f, "Carbohydrate, by difference")
        print(f'\n{f["description"]} (FDC {f["fdcId"]})')
        print(f"  Energy: {kcal} kcal/100g")
        print(f"  Protein: {prot} g/100g")
        print(f"  Fat: {fat} g/100g")
        print(f"  Carbs: {carb} g/100g")

def build_diet(query, target_kcal=2000, items=5):
    foods = search_foods(query, page_size=50)
    scored = []
    for f in foods:
        kcal = get_nutrient(f, "Energy")
        prot = get_nutrient(f, "Protein")
        if not kcal or kcal <= 0 or not prot:
            continue
        scored.append((f, float(kcal), float(prot)))
    if not scored:
        print("No usable foods (missing energy/protein).")
        return
    scored.sort(key=lambda x: x[2] / x[1], reverse=True)  # protein per kcal
    items = min(items, len(scored))
    per_item_kcal = target_kcal / items
    total_kcal = total_prot = 0.0

    print(f"\nDiet plan for query '{query}' targeting ~{target_kcal} kcal/day:")
    for f, kcal100, prot100 in scored[:items]:
        grams = per_item_kcal * 100 / kcal100
        kcal = grams * kcal100 / 100
        prot = grams * prot100 / 100
        total_kcal += kcal
        total_prot += prot
        print(f"\n{f['description']} (FDC {f['fdcId']})")
        print(f"  Portion: {grams:0.1f} g/day")
        print(f"  -> {kcal:0.0f} kcal, {prot:0.1f} g protein")

    print(f"\nApprox total: {total_kcal:0.0f} kcal, {total_prot:0.1f} g protein")

def main():
    if "--diet" in sys.argv:
        args = [a for a in sys.argv[1:] if a != "--diet"]
        query = " ".join(args) or input("Food type / keyword (e.g. 'lentils', 'fruit', 'indian veg'): ")
        try:
            target = float(input("Target kcal per day (default 2000): ") or "2000")
        except ValueError:
            target = 2000.0
        build_diet(query, target_kcal=target)
    else:
        query = " ".join(sys.argv[1:]) or input("Food name to search: ")
        simple_search(query)

if __name__ == "__main__":
    main()
