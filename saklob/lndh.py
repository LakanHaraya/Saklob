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