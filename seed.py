"""
Seed script — populates the Neon PostgreSQL database with the initial
mock data that currently lives in frontend/src/data/index.ts.
"""
import datetime
from database import SessionLocal, engine, Base
import models

# Ensure all tables exist
Base.metadata.create_all(bind=engine)


def seed():
    db = SessionLocal()

    # Skip if data already exists
    if db.query(models.Category).count() > 0:
        print("Database already seeded — skipping.")
        db.close()
        return

    print("Seeding database …")

    # ─── Categories ──────────────────────────────────────────────
    categories = [
        models.Category(id="chemistry-analyzers", name="Chemistry Analyzers", description="Automated biochemistry analyzers for clinical and research laboratories, providing accurate metabolic and enzyme analysis.", image="https://images.unsplash.com/photo-1582719471384-894fbb16e074?w=600&h=400&fit=crop&auto=format", featured=True),
        models.Category(id="hematology-analyzers", name="Hematology Analyzers", description="Complete blood count analyzers for comprehensive blood cell analysis in clinical settings.", image="https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=600&h=400&fit=crop&auto=format", featured=True),
        models.Category(id="coagulation-analyzers", name="Coagulation Analyzers", description="Hemostasis analyzers for thrombosis and hemostasis testing in hospitals and diagnostic labs.", image="https://images.unsplash.com/photo-1576086213369-97a306d36557?w=600&h=400&fit=crop&auto=format", featured=True),
        models.Category(id="immunofluorescence", name="Immunofluorescence", description="Fluorescence-based immunoassay analyzers for accurate quantitative detection of biomarkers.", image="https://images.unsplash.com/photo-1585823190741-80e2aa3cf33c?w=600&h=400&fit=crop&auto=format", featured=True),
        models.Category(id="electrolyte-analyzers", name="Electrolyte Analyzers", description="Ion-selective electrode analyzers for rapid electrolyte and blood gas measurement.", image="https://images.unsplash.com/photo-1530026405186-ed1f139313f3?w=600&h=400&fit=crop&auto=format", featured=True),
        models.Category(id="urine-analyzers", name="Urine Analyzers", description="Automated urine chemistry and sediment analyzers for complete urinalysis workflows.", image="https://images.unsplash.com/photo-1631557932895-6dd20eeaca1c?w=600&h=400&fit=crop&auto=format", featured=True),
        models.Category(id="microscopes", name="Microscopes", description="Professional laboratory and clinical microscopes for pathology, research and education.", image="https://images.unsplash.com/photo-1516979187457-637abb4f9353?w=600&h=400&fit=crop&auto=format", featured=False),
        models.Category(id="diagnostic-equipment", name="Diagnostic Equipment", description="Point-of-care and bedside diagnostic devices for rapid clinical decision making.", image="https://images.unsplash.com/photo-1504439468489-c8920d796a29?w=600&h=400&fit=crop&auto=format", featured=True),
        models.Category(id="blood-glucose", name="Blood Glucose Equipment", description="Glucometers and continuous glucose monitoring systems for diabetes management.", image="https://images.unsplash.com/photo-1631557932895-6dd20eeaca1c?w=600&h=400&fit=crop&auto=format", featured=False),
        models.Category(id="hemoglobin-meters", name="Hemoglobin Meters", description="Portable and benchtop hemoglobin testing devices for anemia screening and monitoring.", image="https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=600&h=400&fit=crop&auto=format", featured=False),
        models.Category(id="ultrasound-imaging", name="Ultrasound & Imaging", description="Portable and cart-based ultrasound systems for obstetrics, cardiology and general imaging.", image="https://images.unsplash.com/photo-1666214280557-f1b5022eb634?w=600&h=400&fit=crop&auto=format", featured=False),
    ]
    db.add_all(categories)
    db.flush()
    print(f"  ✓ {len(categories)} categories")

    # ─── Brands ──────────────────────────────────────────────────
    brands = [
        models.Brand(id="qlabs", name="Qlabs", description="Advanced clinical chemistry and hematology analyzers designed for reliability and performance in busy laboratory environments.", website="Information pending verification", featured=True),
        models.Brand(id="rayto", name="Rayto", description="Professional diagnostic equipment manufacturer providing chemistry analyzers, ELISA readers and laboratory automation solutions.", website="Information pending verification", featured=True),
        models.Brand(id="dirui", name="Dirui", description="Leading manufacturer of urine analyzers, dry chemistry systems, and complete urinalysis solutions for clinical laboratories.", website="Information pending verification", featured=True),
        models.Brand(id="healpoint", name="Healpoint", description="Point-of-care diagnostic solutions including rapid test readers, hemoglobin meters and portable analyzers.", website="Information pending verification", featured=False),
        models.Brand(id="mindray", name="Mindray", description="Global medical device manufacturer offering hematology, chemistry and patient monitoring solutions.", website="Information pending verification", featured=True),
    ]
    db.add_all(brands)
    db.flush()
    print(f"  ✓ {len(brands)} brands")

    # ─── Products ────────────────────────────────────────────────
    products_data = [
        {
            "id": "qlabs-3-pro", "slug": "qlabs-3-pro", "name": "Qlabs 3 Pro",
            "category_id": "chemistry-analyzers", "brand_id": "qlabs",
            "short_description": "Fully automated biochemistry analyzer with 200 tests/hour throughput for mid-to-large clinical laboratories.",
            "description": "The Qlabs 3 Pro is a fully automated clinical chemistry analyzer designed for high-throughput environments. It delivers reliable, accurate results across a comprehensive test menu including liver function, renal function, lipid profiles, glucose, and enzyme panels.",
            "image": "https://images.unsplash.com/photo-1582719471384-894fbb16e074?w=800&h=600&fit=crop&auto=format",
            "featured": True, "published": True, "has_brochure": True,
            "images": [
                "https://images.unsplash.com/photo-1582719471384-894fbb16e074?w=800&h=600&fit=crop&auto=format",
                "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=800&h=600&fit=crop&auto=format",
            ],
            "specifications": [
                {"key": "Testing Method", "value": "Colorimetric / Enzymatic"},
                {"key": "Throughput", "value": "200 tests/hour"},
                {"key": "Sample Types", "value": "Serum, Plasma, Urine, CSF"},
                {"key": "Test Menu", "value": "100+ assay parameters"},
                {"key": "Sample Volume", "value": "2–20 μL"},
                {"key": "Reagent Positions", "value": "40 positions"},
                {"key": "Display", "value": '15" Touch Screen'},
                {"key": "Connectivity", "value": "LIS, USB, Ethernet"},
                {"key": "Power", "value": "220V AC, 50Hz"},
            ],
            "features": [
                "Fully automated sample and reagent handling",
                "Onboard reagent cooling for stability",
                "Real-time quality control monitoring",
                "Bidirectional LIS connectivity",
                "Automatic sample dilution and reruns",
                "Comprehensive test menu with open reagent system",
            ],
            "applications": ["Clinical chemistry", "Metabolic panels", "Liver function testing", "Renal function testing", "Lipid profiling"],
            "benefits": [
                "Reduces manual intervention and operator errors",
                "High throughput for busy laboratory environments",
                "Open system compatibility with multiple reagent brands",
                "Reliable results with onboard QC monitoring",
            ],
        },
        {
            "id": "rayto-rt-9600", "slug": "rayto-rt-9600", "name": "Rayto RT-9600",
            "category_id": "chemistry-analyzers", "brand_id": "rayto",
            "short_description": "Semi-automated chemistry analyzer ideal for small to medium clinical laboratories and clinics.",
            "description": "The Rayto RT-9600 is a reliable semi-automated biochemistry analyzer offering accurate results for routine clinical chemistry testing. Ideal for smaller laboratories requiring dependable performance at an accessible entry point.",
            "image": "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=800&h=600&fit=crop&auto=format",
            "featured": True, "published": True, "has_brochure": False,
            "images": ["https://images.unsplash.com/photo-1576086213369-97a306d36557?w=800&h=600&fit=crop&auto=format"],
            "specifications": [
                {"key": "Testing Method", "value": "Photometric"},
                {"key": "Throughput", "value": "Up to 60 tests/hour"},
                {"key": "Sample Types", "value": "Serum, Plasma, Urine"},
                {"key": "Wavelengths", "value": "8 fixed wavelengths"},
                {"key": "Display", "value": "LCD Display"},
                {"key": "Connectivity", "value": "RS-232, USB"},
                {"key": "Power", "value": "220V AC"},
            ],
            "features": [
                "Stable optical system",
                "User-defined open channel programming",
                "Automatic blank measurement",
                "Statistical quality control",
                "Multiple calculation modes",
            ],
            "applications": ["Routine clinical chemistry", "Enzyme assays", "Turbidimetry", "Electrolyte analysis"],
            "benefits": [
                "Affordable entry point for smaller facilities",
                "Simple operation with minimal training required",
                "Reliable and consistent results",
            ],
        },
        {
            "id": "qlabs-h500", "slug": "qlabs-h500", "name": "Qlabs H500",
            "category_id": "hematology-analyzers", "brand_id": "qlabs",
            "short_description": "5-part differential hematology analyzer with 60 samples/hour for comprehensive blood count analysis.",
            "description": "The Qlabs H500 delivers comprehensive CBC with 5-part differential analysis, providing detailed blood cell data essential for clinical diagnosis. Designed for clinical laboratories requiring reliable and fast hematology results.",
            "image": "https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=800&h=600&fit=crop&auto=format",
            "featured": True, "published": True, "has_brochure": True,
            "images": ["https://images.unsplash.com/photo-1559757175-0eb30cd8c063?w=800&h=600&fit=crop&auto=format"],
            "specifications": [
                {"key": "Parameters", "value": "29 CBC + 3-part/5-part diff"},
                {"key": "Throughput", "value": "60 samples/hour"},
                {"key": "Sample Volume", "value": "20 μL (whole blood)"},
                {"key": "Sample Mode", "value": "Venous and Capillary"},
                {"key": "Display", "value": '10.4" Color Touch Screen'},
                {"key": "Data Storage", "value": "100,000 results"},
                {"key": "Connectivity", "value": "LIS, USB, Ethernet"},
            ],
            "features": [
                "5-part differential leukocyte analysis",
                "Reticulocyte channel for anemia monitoring",
                "Automatic sample aspiration",
                "Built-in thermal printer",
                "Intelligent alarm and flag system",
            ],
            "applications": ["Complete blood count", "Anemia diagnosis", "Infection screening", "Platelet disorders", "Leukemia monitoring"],
            "benefits": [
                "Comprehensive CBC panel for accurate clinical decisions",
                "High throughput for busy hematology labs",
                "Reliable 5-part differential for detailed WBC analysis",
            ],
        },
        {
            "id": "dirui-h800", "slug": "dirui-h800", "name": "Dirui H-800",
            "category_id": "urine-analyzers", "brand_id": "dirui",
            "short_description": "Automated urine chemistry and sediment workstation for complete urinalysis.",
            "description": "The Dirui H-800 provides integrated urine chemistry and sediment analysis in a single automated workstation. Combining strip reading with digital particle classification for a comprehensive urinalysis solution.",
            "image": "https://images.unsplash.com/photo-1631557932895-6dd20eeaca1c?w=800&h=600&fit=crop&auto=format",
            "featured": False, "published": True, "has_brochure": False,
            "images": ["https://images.unsplash.com/photo-1631557932895-6dd20eeaca1c?w=800&h=600&fit=crop&auto=format"],
            "specifications": [
                {"key": "Throughput", "value": "120 samples/hour"},
                {"key": "Parameters", "value": "14 chemistry parameters"},
                {"key": "Sediment Parameters", "value": "12 particle categories"},
                {"key": "Strip Compatibility", "value": "Standard urinalysis strips"},
                {"key": "Display", "value": '12" Touch Screen'},
                {"key": "Connectivity", "value": "LIS, USB, Ethernet"},
            ],
            "features": [
                "Automated strip loading and reading",
                "Integrated sediment analysis module",
                "Digital particle classification with images",
                "Automatic sample transport",
            ],
            "applications": ["Urinalysis", "Kidney disease monitoring", "UTI screening", "Diabetic nephropathy monitoring"],
            "benefits": [
                "Complete urinalysis in one automated system",
                "Reduces manual microscopy workload",
                "Consistent and reproducible results",
            ],
        },
        {
            "id": "healpoint-fq-5000", "slug": "healpoint-fq-5000", "name": "Healpoint FQ-5000",
            "category_id": "immunofluorescence", "brand_id": "healpoint",
            "short_description": "Fluorescence immunoassay analyzer for rapid quantitative cardiac, inflammatory and hormonal biomarker testing.",
            "description": "The Healpoint FQ-5000 is a compact fluorescence immunoassay analyzer delivering quantitative results for a wide range of critical biomarkers at the point of care. Suitable for emergency departments, clinics and small laboratories.",
            "image": "https://images.unsplash.com/photo-1585823190741-80e2aa3cf33c?w=800&h=600&fit=crop&auto=format",
            "featured": True, "published": True, "has_brochure": True,
            "images": ["https://images.unsplash.com/photo-1585823190741-80e2aa3cf33c?w=800&h=600&fit=crop&auto=format"],
            "specifications": [
                {"key": "Detection Method", "value": "Time-resolved fluorescence"},
                {"key": "Result Time", "value": "3–15 minutes"},
                {"key": "Test Menu", "value": "Cardiac, CRP, PCT, Hormones, Thyroid"},
                {"key": "Sample Type", "value": "Whole blood, Serum, Plasma"},
                {"key": "Sample Volume", "value": "75–100 μL"},
                {"key": "Display", "value": '7" Color Touch Screen'},
                {"key": "Connectivity", "value": "LIS, USB, WiFi"},
            ],
            "features": [
                "Quantitative fluorescence detection",
                "Wide test menu for critical biomarkers",
                "Ready-to-use single-use test cassettes",
                "Compact and portable design",
                "Onboard QC and calibration management",
            ],
            "applications": ["Cardiac emergency triage", "Sepsis detection", "Thyroid function", "Inflammatory markers", "Hormonal testing"],
            "benefits": [
                "Fast results for critical clinical decisions",
                "Minimal sample preparation required",
                "Suitable for point-of-care and laboratory use",
            ],
        },
    ]

    for pdata in products_data:
        product = models.Product(
            id=pdata["id"], slug=pdata["slug"], name=pdata["name"],
            category_id=pdata["category_id"], brand_id=pdata["brand_id"],
            short_description=pdata["short_description"],
            description=pdata["description"], image=pdata["image"],
            featured=pdata["featured"], published=pdata["published"],
            has_brochure=pdata["has_brochure"],
        )
        db.add(product)
        db.flush()

        for url in pdata.get("images", []):
            db.add(models.ProductImage(product_id=product.id, url=url))
        for spec in pdata.get("specifications", []):
            db.add(models.ProductSpecification(product_id=product.id, key=spec["key"], value=spec["value"]))
        for feat in pdata.get("features", []):
            db.add(models.ProductFeature(product_id=product.id, feature=feat))
        for app in pdata.get("applications", []):
            db.add(models.ProductApplication(product_id=product.id, application=app))
        for ben in pdata.get("benefits", []):
            db.add(models.ProductBenefit(product_id=product.id, benefit=ben))

    db.flush()
    print(f"  ✓ {len(products_data)} products (with specs, features, etc.)")

    # ─── Solutions ───────────────────────────────────────────────
    solutions_data = [
        {"id": "laboratory", "title": "Laboratory Solutions", "description": "Complete equipment solutions for medical and research laboratories, from chemistry analyzers to complete workflow automation.", "icon": "FlaskConical", "image": "https://images.unsplash.com/photo-1582719471384-894fbb16e074?w=900&h=600&fit=crop&auto=format", "industries": ["Hospitals", "Reference Laboratories", "Research Institutions"]},
        {"id": "diagnostics", "title": "Diagnostic Solutions", "description": "Advanced diagnostic platforms enabling accurate, rapid testing across immunoassay, hematology, and clinical chemistry.", "icon": "Microscope", "image": "https://images.unsplash.com/photo-1576086213369-97a306d36557?w=900&h=600&fit=crop&auto=format", "industries": ["Hospitals", "Clinics", "Diagnostic Centers"]},
        {"id": "hospitals", "title": "Hospital Solutions", "description": "Comprehensive medical and laboratory equipment for hospital departments including emergency, ICU, and wards.", "icon": "Building2", "image": "https://images.unsplash.com/photo-1504439468489-c8920d796a29?w=900&h=600&fit=crop&auto=format", "industries": ["Hospitals", "Government Health Facilities"]},
        {"id": "point-of-care", "title": "Point-of-Care Solutions", "description": "Portable and rapid-result diagnostic tools for bedside testing, primary care and remote health environments.", "icon": "Activity", "image": "https://images.unsplash.com/photo-1585823190741-80e2aa3cf33c?w=900&h=600&fit=crop&auto=format", "industries": ["Clinics", "Outreach Programs", "NGOs"]},
        {"id": "research", "title": "Research & Education Solutions", "description": "Precision laboratory instruments and educational equipment for universities, research centers and training institutions.", "icon": "GraduationCap", "image": "https://images.unsplash.com/photo-1516979187457-637abb4f9353?w=900&h=600&fit=crop&auto=format", "industries": ["Universities", "Research Institutions", "Government Laboratories"]},
    ]
    for sdata in solutions_data:
        sol = models.Solution(id=sdata["id"], title=sdata["title"], description=sdata["description"], icon=sdata["icon"], image=sdata["image"])
        db.add(sol)
        db.flush()
        for ind_name in sdata["industries"]:
            db.add(models.SolutionIndustry(solution_id=sol.id, industry_name=ind_name))
    db.flush()
    print(f"  ✓ {len(solutions_data)} solutions")

    # ─── Industries ──────────────────────────────────────────────
    industries = [
        models.Industry(id="hospitals", name="Hospitals", description="Supporting hospital laboratories, emergency departments and wards with reliable diagnostic and clinical equipment.", icon="Building2", image="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=900&h=600&fit=crop&auto=format"),
        models.Industry(id="laboratories", name="Medical Laboratories", description="Equipping standalone and reference laboratories with high-throughput analyzers and complete laboratory workflow solutions.", icon="FlaskConical", image="https://images.unsplash.com/photo-1582719471384-894fbb16e074?w=900&h=600&fit=crop&auto=format"),
        models.Industry(id="clinics", name="Clinics & Outpatient Centers", description="Compact, easy-to-operate diagnostic solutions tailored for outpatient clinics and primary healthcare facilities.", icon="Stethoscope", image="https://images.unsplash.com/photo-1504439468489-c8920d796a29?w=900&h=600&fit=crop&auto=format"),
        models.Industry(id="research", name="Research Institutions", description="Advanced laboratory instruments supporting scientific research, clinical trials and epidemiological studies.", icon="Microscope", image="https://images.unsplash.com/photo-1516979187457-637abb4f9353?w=900&h=600&fit=crop&auto=format"),
        models.Industry(id="universities", name="Universities & Training", description="Educational and training laboratory equipment for medical schools, nursing colleges and biomedical science programs.", icon="GraduationCap", image="https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=900&h=600&fit=crop&auto=format"),
        models.Industry(id="ngos", name="NGOs & Health Programs", description="Portable and robust diagnostic solutions for public health programs, outreach campaigns and humanitarian healthcare projects.", icon="Heart", image="https://images.unsplash.com/photo-1582560475093-ba66accbc095?w=900&h=600&fit=crop&auto=format"),
    ]
    db.add_all(industries)
    db.flush()
    print(f"  ✓ {len(industries)} industries")



    # ─── Resources ───────────────────────────────────────────────
    resources = [
        models.Resource(id="laboratory-setup-guide", title="Laboratory Setup Guide", description="A practical guide to planning and equipping a clinical laboratory, covering equipment selection, workflow design and quality standards.", category="Guide", date=datetime.date(2024, 1, 1), type="pdf", published=True),
        models.Resource(id="chemistry-analyzer-comparison", title="Choosing the Right Chemistry Analyzer", description="An overview of key considerations when selecting a clinical chemistry analyzer for your laboratory, including throughput, test menu and connectivity.", category="Article", date=datetime.date(2024, 3, 1), type="article", published=True),
        models.Resource(id="poc-diagnostics-overview", title="Point-of-Care Diagnostics: Applications and Considerations", description="Understanding the role of point-of-care diagnostic tools in modern healthcare and how to select the right solution for your environment.", category="Article", date=datetime.date(2024, 6, 1), type="article", published=True),
    ]
    db.add_all(resources)
    db.flush()
    print(f"  ✓ {len(resources)} resources")

    # ─── Quote Requests (sample data) ────────────────────────────
    qr1 = models.QuoteRequest(id="QR-001", name="Dr. Sarah Mwangi", organization="Nairobi General Hospital", email="s.mwangi@nairobigeneral.co.ke", phone="+254 701 234 567", location="Nairobi", product="Qlabs 3 Pro", quantity=2, message="We are looking to upgrade our laboratory. Please provide a quotation including installation and training.", date=datetime.date(2024, 7, 15), status="NEW")
    db.add(qr1)
    db.flush()

    qr2 = models.QuoteRequest(id="QR-002", name="James Otieno", organization="Aga Khan Diagnostic Centre", email="j.otieno@akdn.org", phone="+254 722 345 678", location="Mombasa", product="Healpoint FQ-5000", quantity=1, message="Interested in the immunofluorescence analyzer for our emergency department.", date=datetime.date(2024, 7, 14), status="CONTACTED", assigned_to="Alex K.")
    db.add(qr2)
    db.flush()
    db.add(models.QuoteRequestNote(quote_request_id="QR-002", note="Called on 14th. Client requested demo."))

    qr3 = models.QuoteRequest(id="QR-003", name="Prof. Anne Kamau", organization="University of Nairobi Medical School", email="a.kamau@uon.ac.ke", phone="+254 733 456 789", location="Nairobi", product="Microscopes", quantity=10, message="Procurement for student laboratory. Requires budget-appropriate options.", date=datetime.date(2024, 7, 13), status="QUOTATION SENT", assigned_to="Mary W.")
    db.add(qr3)
    db.flush()
    db.add(models.QuoteRequestNote(quote_request_id="QR-003", note="Quotation emailed 13th July."))
    db.add(models.QuoteRequestNote(quote_request_id="QR-003", note="Follow up scheduled for 20th July."))

    qr4 = models.QuoteRequest(id="QR-004", name="Charles Kiprop", organization="Eldoret Regional Lab", email="c.kiprop@eldoretlab.co.ke", phone="+254 711 567 890", location="Eldoret", product="Qlabs H500", quantity=1, message="Replacing existing CBC analyzer. Need service support in Eldoret.", date=datetime.date(2024, 7, 12), status="NEGOTIATION", assigned_to="Alex K.")
    db.add(qr4)
    db.flush()
    db.add(models.QuoteRequestNote(quote_request_id="QR-004", note="Negotiating service contract terms."))

    qr5 = models.QuoteRequest(id="QR-005", name="Ruth Achieng", organization="AMREF Health Africa", email="r.achieng@amref.org", phone="+254 700 678 901", location="Nairobi", product="Healpoint FQ-5000", quantity=5, message="Field deployment for community health program. Need portable options.", date=datetime.date(2024, 7, 11), status="WON", assigned_to="Mary W.")
    db.add(qr5)
    db.flush()
    db.add(models.QuoteRequestNote(quote_request_id="QR-005", note="Order confirmed. Delivery scheduled for August."))

    db.flush()
    print("  ✓ 5 quote requests")

    db.commit()
    print("\n✅ Database seeded successfully!")
    db.close()


if __name__ == "__main__":
    seed()
