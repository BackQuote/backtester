import React, { PropTypes } from 'react';
import { positive, negative } from '../styles/profitNumber.scss';

class ProfitNumber extends React.Component {
  render() {
    let { value } = this.props;
    return value < 0 ? (
      <span className={negative}>({value}$)</span>
    ) : (
      <span className={positive}>{value}$</span>
    );
  }
}

export default ProfitNumber;
