def irehistro_lndh(konteksto_rehistro):
    konteksto_rehistro.idagdag(
        "saklob",
        ["dron"]
    )

    konteksto_rehistro.idagdag(
        "saklob:dron",
        ["kom", "masid"]
    )

    konteksto_rehistro.idagdag(
        "saklob:dron:kom",
        ["radyo"]
    )

    konteksto_rehistro.idagdag(
        "saklob:dron:masid",
        []
    )

    konteksto_rehistro.idagdag(
        "saklob:dron:kom:radyo",
        []
    )

    konteksto_rehistro.itakda_deskripsiyon(
        "saklob:dron",
        "LNDH dron."
    )

    konteksto_rehistro.itakda_deskripsiyon(
        "saklob:dron:kom",
        "Komunikasyon ng dron."
    )

    konteksto_rehistro.itakda_deskripsiyon(
        "saklob:dron:masid",
        "Pagmamasid ng dron."
    )

    konteksto_rehistro.itakda_deskripsiyon(
        "saklob:dron:kom:radyo",
        "Radyo ng komunikasyon."
    )