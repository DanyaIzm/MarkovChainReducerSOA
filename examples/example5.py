from markov_chain_reducer_soa import MarkovChainReducer, Link


def main():
    link12 = Link(1, 1)
    link22 = Link(0.62, 1)
    link23 = Link(0.38, 2)
    link33 = Link(0.81, 2)
    link34 = Link(0.19, 1)
    link44 = Link(0.31, 4)
    link45 = Link(0.69, 1)

    link23 = MarkovChainReducer.reduce_loop_link(link22, link23)
    link34 = MarkovChainReducer.reduce_loop_link(link33, link34)
    link45 = MarkovChainReducer.reduce_loop_link(link44, link45)

    link35 = MarkovChainReducer.reduce_unit_links(link34, link45)
    link25 = MarkovChainReducer.reduce_unit_links(link23, link35)
    link15 = MarkovChainReducer.reduce_unit_links(link12, link25)

    print(MarkovChainReducer.round_link(link15))


if __name__ == "__main__":
    main()
