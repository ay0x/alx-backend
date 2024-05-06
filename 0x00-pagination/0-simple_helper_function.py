def index_range(page, page_size):
    if page < 1 or page_size < 1:
        raise ValueError("Page and page_size must be positive integers")
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index
