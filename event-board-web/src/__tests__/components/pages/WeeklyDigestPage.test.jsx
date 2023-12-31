import React from 'react';
import { render, screen } from '@testing-library/react';
import WeeklyDigestPage from 'components/pages/WeeklyDigestPage';

jest.mock('hooks/authentication', () => ({
  useAuth: () => ({
    currentUser: { isAuthenticated: false },
    verifyOneTimePassCode: jest.fn(),
  }),
}));

describe('Weekly digest sign up', () => {
  it('renders heading', () => {
    render(<WeeklyDigestPage />);

    expect(screen.getByText(/Subscribe to our Weekly Digest/i))
      .toBeInTheDocument();
  });
});
