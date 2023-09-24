from markov_chain_reducer_soa import MarkovChainReducer, Link


def main():
    link12 = Link(1, 1)
    link23 = Link(0.1, 2)
    link24 = Link(0.9, 1)
    link33 = Link(0.59, 3)
    link34 = Link(0.41, 4)
    link44 = Link(0.35, 4)
    link45 = Link(0.65, 3)

    link45 = MarkovChainReducer.reduce_loop_link(link44, link45)
    link34 = MarkovChainReducer.reduce_loop_link(link33, link34)

    print("Link45 " + str(link45))
    print("Link34 " + str(link34))

    link24_new = MarkovChainReducer.reduce_unit_links(link23, link34)

    print("Link24_new " + str(link24_new))

    link24 = MarkovChainReducer.reduce_parallel_links(link24, link24_new)

    print("Link24 " + str(link24))

    link25 = MarkovChainReducer.reduce_unit_links(link24, link45)

    print("Link25 " + str(link25))

    link15 = MarkovChainReducer.reduce_unit_links(link12, link25)

    print("Link15 " + str(MarkovChainReducer.round_link(link15)))


if __name__ == "__main__":
    main()
