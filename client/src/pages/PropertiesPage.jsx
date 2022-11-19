import { Col, Container, Row } from 'react-bootstrap';
import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import Spinner from '../components/Spinner';
import { getProperties } from '../features/properties/propertySlice';

const PropertiesPage = () => {
  const { propertiesList, isLoading } = useSelector(
    (state) => state.propertiesList
  );

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getProperties());
  }, [dispatch]);

  if (isLoading) {
    return <Spinner />;
  }

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
