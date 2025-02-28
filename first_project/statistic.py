def get_stat_dict(characteristics_:dict)->dict:


    stat_dict = {
        "avg_diag": [],
        "avg_volume": [],
        "avg_surface_area": [],
        "avg_alpha":[],
        "avg_beta":[],
        "avg_gamma": [],
        "avg_radius_described_sphere": [],
        "avg_volume_described_sphere": []
    }

    for fig in characteristics_.values():
        stat_dict["avg_diag"].append(float(fig['diag']))
        stat_dict["avg_volume"].append(float(fig['volume']))
        stat_dict["avg_surface_area"].append(float(fig['surface_area']))
        stat_dict["avg_alpha"].append(float(fig['alpha']))
        stat_dict["avg_beta"].append(float(fig['beta']))
        stat_dict["avg_gamma"].append(float(fig['gamma']))
        stat_dict["avg_radius_described_sphere"].append(float(fig['radius_described_sphere']))
        stat_dict["avg_volume_described_sphere"].append(float(fig['volume_described_sphere']))

    statistics = {k: str(round(sum(v)/len(v), 2)) for k, v in stat_dict.items()}