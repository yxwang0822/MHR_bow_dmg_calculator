def bow_dmg_calculator(total_phys_dmg,
                       total_elem_dmg,
                       action_value,
                       phys_additions,
                       elem_additions,
                       crit_prob,
                       crit_power,
                       phys_abs,
                       elem_abs):
    """

    :param total_phys_dmg:
    :param total_elem_dmg:
    :param action_value:
    :param phys_additions:
    :param elem_additions:
    :param crit_prob:
    :param crit_power:
    :param phys_abs:
    :param elem_abs:
    :return:
    """
    phys_dmg_non_crit = round((total_phys_dmg / 100) * 1.7 * phys_additions * action_value * phys_abs / 100)

    phys_dmg_crit = round((total_phys_dmg / 100) * 1.7 * phys_additions * action_value * crit_power * phys_abs / 100)

    elem_dmg = round(total_elem_dmg * 1.125 * elem_additions * elem_abs / 100)

    expect_dmg = phys_dmg_crit * crit_prob + phys_dmg_non_crit * (1 - crit_prob) + elem_dmg

    return phys_dmg_crit, phys_dmg_non_crit, elem_dmg, expect_dmg

