from markov_chain_reducer_soa import Link, MarkovChainReducer


def task1():
    link12 = Link(1, 2)
    link23 = Link(0.8, 3)
    link32 = Link(0.7, 4)
    link24 = Link(0.2, 5)
    link34 = Link(0.3, 1)

    link24new, link22 = MarkovChainReducer.reduce_unit_with_fb_loop_link(
        link34, link23, link32
    )
    print("Удаление межзвенной связи и звена 23<>32->34: ")
    print("Новая 24 связь ", link24new)
    print("Связь 22 ", link22)

    link24 = MarkovChainReducer.reduce_parallel_links(link24, link24new)
    print("Удаление параллельных путей 24||24 ", link24)

    link24 = MarkovChainReducer.reduce_loop_link(link22, link24)
    print("Удаление петли 22 ", link24)

    link14 = MarkovChainReducer.reduce_unit_links(link12, link24)
    print("Удаление финального звена 1->(|2|)->4", link14)

    link14 = MarkovChainReducer.round_link(link14, ndigits=3)

    print("Ответ: ", link14)


if __name__ == "__main__":
    task1()
