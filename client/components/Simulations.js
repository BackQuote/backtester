import React, { PropTypes } from 'react';
import { card } from '../styles/card.scss';
import SimulationRow from './SimulationRow';

class Simulations extends React.Component {
  render() {
    return (
      <div className={card}>
        <header>
          <h4 className="title">
            Simulations
          </h4>
        </header>
        <section>
          <table className="u-full-width">
            <thead>
            <tr>
              <th>Simulation</th>
              <th>Algorithm</th>
              <th>Parameters</th>
              <th>Tickers</th>
            </tr>
            </thead>
            <tbody>
            {
              this.props.simulations.map((simulation) => {
                return <SimulationRow simulation={simulation}/>;
              })
            }
            </tbody>
          </table>
        </section>
      </div>
    );
  }
}

Simulations.propTypes = {
  simulations: PropTypes.array
};

export default Simulations;