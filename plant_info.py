# Dictionary containing medicinal information for each plant class
PLANT_INFO = {
    'Aloevera': {
        'scientific_name': 'Aloe barbadensis miller',
        'description': 'A succulent plant species of the genus Aloe. It is widely distributed, and is considered an invasive species in many world regions.',
        'uses': [
            'Treats sunburns and skin injuries',
            'Moisturizes skin',
            'Digestive aid',
            'Boosts immune system'
        ]
    },
    'Amla': {
        'scientific_name': 'Phyllanthus emblica',
        'description': 'Also known as Indian gooseberry, it is a tree that is native to tropical Asia.',
        'uses': [
            'High Vitamin C content',
            'Boosts immunity',
            'Improves hair and skin health',
            'Aids digestion'
        ]
    },
    'Amruta_Balli': {
        'scientific_name': 'Tinospora cordifolia',
        'description': 'Commonly known as Giloy or Guduchi, it is a herbaceous vine of the family Menispermaceae indigenous to tropical areas of India, Myanmar and Sri Lanka.',
        'uses': [
            'Boosts immunity',
            'Treats chronic fever',
            'Improves digestion',
            'Reduces stress and anxiety'
        ]
    },
    'Arali': {
        'scientific_name': 'Nerium oleander',
        'description': 'A shrub or small tree in the dogbane family Apocynaceae, toxic in all its parts.',
        'uses': [
            'Used in traditional medicine (with caution due to toxicity)',
            'Treats skin diseases (external)',
            'Anti-inflammatory properties',
            'Used in treating cardiac insufficiency (historically)'
        ]
    },
    'Ashoka': {
        'scientific_name': 'Saraca asoca',
        'description': 'A plant belonging to the Detarioideae subfamily of the legume family.',
        'uses': [
            'Treats gynecological problems',
            'Pain relief',
            'Improves skin complexion',
            'Anti-inflammatory'
        ]
    },
    'Ashwagandha': {
        'scientific_name': 'Withania somnifera',
        'description': 'An annual evergreen shrub in the Solanaceae or nightshade family that grows in India, the Middle East, and parts of Africa.',
        'uses': [
            'Reduces stress and anxiety',
            'Boosts testosterone and fertility in men',
            'Increases muscle mass and strength',
            'Improves brain function'
        ]
    },
    'Avacado': {
        'scientific_name': 'Persea americana',
        'description': 'A tree originating in the Americas which is likely native to the highland regions of south-central Mexico to Guatemala.',
        'uses': [
            'Rich in nutrients and healthy fats',
            'Improves heart health',
            'High in antioxidants',
            'Good for skin health'
        ]
    },
    'Bamboo': {
        'scientific_name': 'Bambusoideae',
        'description': 'A subfamily of tall treelike grasses of the family Poaceae.',
        'uses': [
            'Young shoots are edible',
            'Leaves used for fever and detoxification',
            'Treats respiratory issues',
            'Promotes wound healing'
        ]
    },
    'Basale': {
        'scientific_name': 'Basella alba',
        'description': 'Also known as Malabar spinach, it is an edible perennial vine in the family Basellaceae.',
        'uses': [
            'Rich in Vitamin A and C',
            'Cools the body',
            'Treats mouth ulcers',
            'Good for digestion'
        ]
    },
    'Betel': {
        'scientific_name': 'Piper betle',
        'description': 'A vine of the family Piperaceae, which includes pepper and kava.',
        'uses': [
            'Mouth freshener',
            'Aids digestion',
            'Antiseptic properties',
            'Relieves cough'
        ]
    },
    'Betel_Nut': {
        'scientific_name': 'Areca catechu',
        'description': 'The seed of the areca palm, which grows in much of the tropical Pacific, Southeast and South Asia, and parts of east Africa.',
        'uses': [
            'Stimulant',
            'Aids digestion',
            'Strengthens gums (traditional)',
            'Used in deworming'
        ]
    },
    'Brahmi': {
        'scientific_name': 'Bacopa monnieri',
        'description': 'A perennial, creeping herb native to the wetlands of southern and Eastern India, Australia, Europe, Africa, Asia, and North and South America.',
        'uses': [
            'Enhances memory and cognitive function',
            'Reduces anxiety and stress',
            'Anti-inflammatory',
            'Antioxidant properties'
        ]
    },
    'Castor': {
        'scientific_name': 'Ricinus communis',
        'description': 'A species of flowering plant in the spurge family, Euphorbiaceae.',
        'uses': [
            'Laxative properties',
            'Promotes hair growth',
            'Treats skin infections',
            'Relieves joint pain'
        ]
    },
    'Curry_Leaf': {
        'scientific_name': 'Murraya koenigii',
        'description': 'A tropical to sub-tropical tree in the family Rutaceae, which is native to India.',
        'uses': [
            'Flavoring agent',
            'Rich in antioxidants',
            'Good for hair growth',
            'Aids digestion'
        ]
    },
    'Doddapatre': {
        'scientific_name': 'Plectranthus amboinicus',
        'description': 'Also known as Mexican mint, Spanish thyme, or Indian borage.',
        'uses': [
            'Treats cough and cold',
            'Relieves respiratory issues',
            'Aids digestion',
            'Skin treatment'
        ]
    },
    'Ekka': {
        'scientific_name': 'Calotropis gigantea',
        'description': 'Also known as crown flower, it is a species of Calotropis native to Cambodia, Vietnam, Bangladesh, Indonesia, Malaysia, the Philippines, Thailand, Sri Lanka, India, China, Pakistan, and Nepal.',
        'uses': [
            'Treats joint pain',
            'Anti-inflammatory',
            'Treats skin diseases',
            'Used in digestive disorders'
        ]
    },
    'Ganike': {
        'scientific_name': 'Solanum nigrum',
        'description': 'Commonly known as European black nightshade or locally as Ganike.',
        'uses': [
            'Treats stomach ulcers',
            'Anti-inflammatory',
            'Good for liver health',
            'Treats skin diseases'
        ]
    },
    'Gauva': {
        'scientific_name': 'Psidium guajava',
        'description': 'A common tropical fruit cultivated in many tropical and subtropical regions.',
        'uses': [
            'Leaves treat diarrhea',
            'Lowers blood sugar levels',
            'Boosts heart health',
            'Relieves menstrual symptoms'
        ]
    },
    'Geranium': {
        'scientific_name': 'Pelargonium',
        'description': 'A genus of flowering plants which includes about 200 species of perennials, succulents, and shrubs.',
        'uses': [
            'Aromatherapy (stress relief)',
            'Anti-inflammatory',
            'Antiseptic properties',
            'Skin care'
        ]
    },
    'Henna': {
        'scientific_name': 'Lawsonia inermis',
        'description': 'A flowering plant and the sole species of the Lawsonia genus.',
        'uses': [
            'Natural dye for hair and skin',
            'Cooling effect on skin',
            'Treats headaches',
            'Antifungal properties'
        ]
    },
    'Hibiscus': {
        'scientific_name': 'Hibiscus rosa-sinensis',
        'description': 'A genus of flowering plants in the mallow family, Malvaceae.',
        'uses': [
            'Lowers blood pressure',
            'Promotes hair growth',
            'Rich in antioxidants',
            'Supports liver health'
        ]
    },
    'Honge': {
        'scientific_name': 'Pongamia pinnata',
        'description': 'A species of tree in the pea family, Fabaceae, native to eastern and tropical Asia.',
        'uses': [
            'Oil used for skin diseases',
            'Treats rheumatism',
            'Anti-inflammatory',
            'Wound healing'
        ]
    },
    'Insulin': {
        'scientific_name': 'Chamaecostus cuspidatus',
        'description': 'Commonly known as fiery costus or insulin plant, native to eastern Brazil.',
        'uses': [
            'Regulates blood sugar levels',
            'Anti-diabetic properties',
            'Antioxidant',
            'Anti-microbial'
        ]
    },
    'Jasmine': {
        'scientific_name': 'Jasminum',
        'description': 'A genus of shrubs and vines in the olive family.',
        'uses': [
            'Aromatherapy (relieves stress)',
            'Antiseptic',
            'Treats skin infections',
            'Boosts mood'
        ]
    },
    'Lemon': {
        'scientific_name': 'Citrus limon',
        'description': 'A species of small evergreen tree in the flowering plant family Rutaceae.',
        'uses': [
            'Rich in Vitamin C',
            'Boosts immunity',
            'Aids digestion',
            'Skin care'
        ]
    },
    'Lemon_grass': {
        'scientific_name': 'Cymbopogon',
        'description': 'A genus of Asian, African, Australian, and tropical island plants in the grass family.',
        'uses': [
            'Relieves anxiety',
            'Lowers cholesterol',
            'Pain relief',
            'Boosts oral health'
        ]
    },
    'Mango': {
        'scientific_name': 'Mangifera indica',
        'description': 'A species of flowering plant in the sumac and poison ivy family Anacardiaceae.',
        'uses': [
            'Leaves regulate diabetes',
            'Rich in vitamins',
            'Aids digestion',
            'Boosts immunity'
        ]
    },
    'Mint': {
        'scientific_name': 'Mentha',
        'description': 'A genus of plants in the family Lamiaceae.',
        'uses': [
            'Aids digestion',
            'Relieves cold symptoms',
            'Oral health',
            'Relieves headaches'
        ]
    },
    'Nagadali': {
        'scientific_name': 'Ruta graveolens',
        'description': 'Also known as Rue, it is an ornamental and medicinal herb.',
        'uses': [
            'Treats neuromuscular problems',
            'Anti-inflammatory',
            'Antifungal',
            'Insect repellent'
        ]
    },
    'Neem': {
        'scientific_name': 'Azadirachta indica',
        'description': 'A tree in the mahogany family Meliaceae.',
        'uses': [
            'Antibacterial and antifungal',
            'Treats skin disorders',
            'Boosts immunity',
            'Dental health'
        ]
    },
    'Nithyapushpa': {
        'scientific_name': 'Catharanthus roseus',
        'description': 'Commonly known as Madagascar periwinkle.',
        'uses': [
            'Treats diabetes',
            'Anti-cancer properties (source of vincristine)',
            'Relieves sore throat',
            'Wound healing'
        ]
    },
    'Nooni': {
        'scientific_name': 'Morinda citrifolia',
        'description': 'Also known as Noni, a fruit-bearing tree in the coffee family.',
        'uses': [
            'Boosts immunity',
            'Pain relief',
            'Skin health',
            'Anti-aging'
        ]
    },
    'Pappaya': {
        'scientific_name': 'Carica papaya',
        'description': 'The plant species Carica papaya, one of the 22 accepted species in the genus Carica.',
        'uses': [
            'Leaf extract increases platelet count',
            'Aids digestion',
            'Anti-inflammatory',
            'Rich in antioxidants'
        ]
    },
    'Pepper': {
        'scientific_name': 'Piper nigrum',
        'description': 'A flowering vine in the family Piperaceae, cultivated for its fruit.',
        'uses': [
            'Improves digestion',
            'Relieves cold and cough',
            'Antioxidant properties',
            'Enhances nutrient absorption'
        ]
    },
    'Pomegranate': {
        'scientific_name': 'Punica granatum',
        'description': 'A fruit-bearing deciduous shrub in the family Lythraceae.',
        'uses': [
            'Rich in antioxidants',
            'Anti-inflammatory',
            'Heart health',
            'Improves memory'
        ]
    },
    'Raktachandini': {
        'scientific_name': 'Pterocarpus santalinus',
        'description': 'Also known as Red Sanders or Red Sandalwood.',
        'uses': [
            'Treats skin diseases',
            'Cooling effect',
            'Blood purifier',
            'Anti-inflammatory'
        ]
    },
    'Rose': {
        'scientific_name': 'Rosa',
        'description': 'A woody perennial flowering plant of the genus Rosa, in the family Rosaceae.',
        'uses': [
            'Skin care (rose water)',
            'Stress relief',
            'Digestive aid',
            'Sore throat relief'
        ]
    },
    'Sapota': {
        'scientific_name': 'Manilkara zapota',
        'description': 'A long-lived, evergreen tree native to southern Mexico, Central America and the Caribbean.',
        'uses': [
            'Energy booster',
            'Anti-inflammatory',
            'Good for digestion',
            'Bone health'
        ]
    },
    'Tulasi': {
        'scientific_name': 'Ocimum tenuiflorum',
        'description': 'Commonly known as Holy Basil, an aromatic perennial plant in the family Lamiaceae.',
        'uses': [
            'Treats respiratory disorders',
            'Boosts immunity',
            'Reduces stress',
            'Dental health'
        ]
    },
    'Wood_sorel': {
        'scientific_name': 'Oxalis',
        'description': 'A large genus of flowering plants in the wood-sorrel family Oxalidaceae.',
        'uses': [
            'Rich in Vitamin C',
            'Diuretic properties',
            'Treats fever',
            'Soothes skin irritations'
        ]
    },
    'labels': {
        'scientific_name': 'N/A',
        'description': 'Label file or unknown class.',
        'uses': []
    }
}
