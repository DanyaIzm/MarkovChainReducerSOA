from markov_chain_reducer_soa import MarkovChainReducer, Link


def main():
    link12 = Link(1, 1)
    link23 = Link(0.18, 2)
    link24 = Link(0.82, 1)
    link34 = Link(1, 2)
    link43 = Link(0.94, 2)
    link45 = Link(0.06, 4)

    link24_new, link44 = MarkovChainReducer.reduce_unit_with_fb_loop_link(
        link23, link34, link43
    )

    print(link44)

    link45 = MarkovChainReducer.reduce_loop_link(link44, link45)

    print(link45)

    link24 = MarkovChainReducer.reduce_parallel_links(link24_new, link24)

    link25 = MarkovChainReducer.reduce_unit_links(link24, link45)

    link15 = MarkovChainReducer.reduce_unit_links(link12, link25)

    print(MarkovChainReducer.round_link(link15))


if __name__ == "__main__":
    main()
