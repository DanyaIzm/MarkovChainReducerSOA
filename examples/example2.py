from markov_chain_reducer_soa import Link, MarkovChainReducer


def task2():
    link12 = Link(1, 3)
    link23 = Link(1, 2)
    link32 = Link(0.1, 3)
    link34 = Link(0.6, 4)
    link35 = Link(0.3, 5)
    link43 = Link(0.1, 2)
    link45 = Link(0.9, 3)

    link35new, link33 = MarkovChainReducer.reduce_unit_with_fb_loop_link(
        link45, link34, link43
    )

    print(link33, link35new)

    link35 = MarkovChainReducer.reduce_parallel_links(link35, link35new)

    print(link35)

    link35 = MarkovChainReducer.reduce_loop_link(link33, link35)

    print(link35)

    link25, link22 = MarkovChainReducer.reduce_unit_with_fb_loop_link(
        link35, link23, link32
    )

    print(link22, link25)

    link25 = MarkovChainReducer.reduce_loop_link(link22, link25)

    print(link25)

    link15 = MarkovChainReducer.reduce_unit_links(link12, link25)

    print(link15)

    print(MarkovChainReducer.round_link(link15))


if __name__ == "__main__":
    task2()
