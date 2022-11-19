import { Col, Container, Row } from 'react-bootstrap';
import React from 'react';

const PropertiesPage = () => {
  return (
    <>
      <Container>
        <Row>
          <Col className='mg-top text-center'>
            <h1>Our Catalog of properties</h1>
            <hr className='hr-text' />
          </Col>
        </Row>
      </Container>
    </>
  );
};

export default PropertiesPage;
